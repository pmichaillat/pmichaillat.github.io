# to run from the console:
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# export FRED_API_KEY= 'key'
# python3 dashboard.py

import os
from datetime import datetime
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
import plotly.graph_objects as go

print("Script starting...")

# Load FRED API key
load_dotenv()
apikey = os.getenv("FRED_API_KEY")
if apikey:
    print("FRED_API_KEY environment variable found.")
    print(f"FRED_API_KEY preview: ...{apikey[-4:]}")
else:
    print("FRED_API_KEY environment variable NOT FOUND.")
fred = Fred(api_key=apikey)
print("FRED object initialized.")

# Get the absolute directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to get to the repository root
REPO_ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))

# Define the output directory relative to the repository root
OUTPUT_DIR_ABSOLUTE = os.path.join(REPO_ROOT_DIR, 'static', 'dashboard')

# Ensure output directory exists
print(f"Ensuring output directory exists: {OUTPUT_DIR_ABSOLUTE}")
os.makedirs(OUTPUT_DIR_ABSOLUTE, exist_ok=True)

# Create helper function to fetch recessions
def get_recession_periods(rec_series):
    in_recession = rec_series == 1
    rec_series = rec_series.loc[rec_series.first_valid_index():rec_series.last_valid_index()]
    shifts = in_recession.astype(int).diff()

    starts = rec_series.index[shifts == 1]
    ends = rec_series.index[shifts == -1] - pd.offsets.MonthBegin(1)

    # Handle edge cases where recession starts at the beginning or is ongoing
    if in_recession.iloc[0]:
        starts = starts.insert(0, rec_series.index[0])
    if len(ends) < len(starts):
        ends = ends.insert(len(ends), rec_series.index[-1])

    return zip(starts, ends)

# Create function to make plots
def make_plot(df, y_column, title, filename, y_label, x_min=None, x_max=None, y_min=None, y_max=None, hline=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df[y_column],
        mode='lines',
        line=dict(color='#59539d', width=3),
        hovertemplate='%{x|%b %Y}<br>%{y:.2f}<extra></extra>'
    ))

    # Shade recession months
    try:
        rec = fred.get_series("USREC", observation_start=df.index.min(), observation_end=df.index.max())
        rec.index = pd.to_datetime(rec.index)
        for start, end in get_recession_periods(rec):
            fig.add_vrect(
                x0=start,
                x1=end,
                fillcolor='lightgray',
                opacity=0.3,
                layer='below',
                line_width=0
            )
    except Exception as e:
        print(f"Could not retrieve recession data: {e}")

    if hline is not None:
        fig.add_shape(
            type='line',
            x0=df.index.min(),
            x1=df.index.max(),
            y0=hline,
            y1=hline,
            line=dict(color='rgba(217, 95, 2, 0.7)', width=1),
            layer='above'
            )

    fig.update_layout(
        title=title,
        dragmode=False,
        title_font=dict(size=16),
        font=dict(family="Helvetica", size=16),
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            title_font=dict(size=16),
            tickfont=dict(size=16),
            showgrid=True,
            side='bottom',
            showline=True, 
            linecolor='#e9e9e9',
            mirror=False,
            ticklabelposition="outside",
            ticklabelstandoff=10,
            gridcolor='#e9e9e9',
            range=[x_min, x_max] if x_min is not None and x_max is not None  else None
        ),
        yaxis=dict(
            title_font=dict(size=16),
            tickfont=dict(size=16),
            showgrid=True, 
            side='left',
            showline=True, 
            linecolor='#e9e9e9',
            mirror=False,
            ticklabelposition="outside",
            ticklabelstandoff=10,
            gridcolor='#e9e9e9',
            range=[y_min, y_max] if y_min is not None and y_max is not None else None
        ),
       yaxis_title=dict(
            text=y_label,
            font=dict(size=16)
        ),
        showlegend=False
    )

    # Construct the absolute path for the figure HTML
    html_file_path = os.path.join(OUTPUT_DIR_ABSOLUTE, f"{filename}.html")
    
    fig.write_html(
        html_file_path,
        include_plotlyjs='cdn',
        full_html=False,
        config={
            "displaylogo": False,
            "modeBarButtonsToRemove": [
            "zoomIn2d",
            "zoomOut2d",
            "autoscale" 
            ],
            "toImageButtonOptions": {
            "format": "png",
            "filename": filename,
            "height": 900,
            "width": 1200,
            "scale": 3
            }
        }
    )

    print(f"Successfully wrote HTML: {html_file_path}")


# Fetch raw data from FRED
u = fred.get_series("UNEMPLOY")
if u is not None and not u.empty:
    print(f"UNEMPLOY data fetched successfully. Shape: {u.shape}, Last date: {u.index.max()}")
    u.index = pd.to_datetime(u.index)
    latest_u_date = u.index.max()
    latest_u_value = u.iloc[-1]
    print(f"UNEMPLOY raw latest point: Date='{latest_u_date.strftime('%Y-%m-%d')}', Value='{latest_u_value}'")
else:
    print("Failed to fetch UNEMPLOY data or data is empty.")

v = fred.get_series("JTSJOL")
if v is not None and not v.empty:
    print(f"JTSJOL data fetched successfully. Shape: {v.shape}, Last date: {v.index.max()}")
    v.index = pd.to_datetime(v.index)
    latest_v_date = v.index.max()
    latest_v_value = v.iloc[-1]
    previous_v_value = v.iloc[-2]
    print(f"JTSJOL raw latest point: Date='{latest_v_date.strftime('%Y-%m-%d')}', Latest value='{latest_v_value}', Previous value='{previous_v_value}'")
else:
    print("Failed to fetch JTSJOL data or data is empty.")

lf = fred.get_series("CLF16OV")
if lf is not None and not lf.empty:
    print(f"CLF16OV data fetched successfully. Shape: {lf.shape}, Last date: {lf.index.max()}")
    lf.index = pd.to_datetime(lf.index)
    latest_lf_date = lf.index.max()
    latest_lf_value = lf.iloc[-1]
    print(f"CLF16OV raw latest point: Date='{latest_lf_date.strftime('%Y-%m-%d')}', Value='{latest_lf_value}'")

else:
    print("Failed to fetch CLF16OV data or data is empty.")

# Extend vacancy index by 1 month at the end
last_date = v.index.max()
next_date = last_date + pd.offsets.MonthBegin(1)

# Append NaN at the new date
v_extended = v.reindex(v.index.union([next_date]))

# Now shift vacancy values forward by 1 month
v_shifted = v_extended.shift(1)

data = pd.concat([u, v_shifted, lf], axis=1, join='inner')
data.columns = ['u', 'v', 'lf']
data = data.dropna()

# Compute simple variables
u_rate = (data['u'] / data['lf']) * 100
v_rate = (data['v'] / data['lf']) * 100
tightness = v_rate / u_rate
feru = (u_rate * v_rate).pow(0.5)
u_gap = u_rate - feru

# Compute Michez-rule variables
# Compute 3-month trailing average of unemployment rate
u_bar = u_rate.rolling(window=3, min_periods=1).mean()

# Compute unemployment indicator
u_hat_exact = u_bar - u_bar.rolling(window=13, min_periods=1).min()

# Round to 2 decimal places (basis point precision)
u_hat = u_hat_exact.round(2)

# Compute 3-month trailing average of vacancy rate
v_bar = v_rate.rolling(window=3, min_periods=1).mean()

# Compute vacancy indicator
v_hat_exact = v_bar.rolling(window=13, min_periods=1).max() - v_bar

# Round to 2 decimal places (basis point precision)
v_hat = v_hat_exact.round(2)

# Compute minimum indicator
m = pd.DataFrame({'u_hat': u_hat, 'v_hat': v_hat}).min(axis=1)

# Compute recession probability
p_exact = (m - 0.29) / (0.81 - 0.29)

# Clamp values between 0 and 1
p_exact = p_exact.clip(lower=0, upper=1) * 100

# Round to 1 decimal place
p = p_exact.round(1)

# Plot unemployment rate

df = pd.DataFrame({"data": u_rate}).dropna()

if not df.empty:
    latest_processed_u_date = df.index.max()
    latest_processed_u_value = df['data'].iloc[-1]
    previous_processed_u_value = df['data'].iloc[-2]
    print(f"Unemployment rate latest processed point for CSV: Date='{latest_processed_u_date.strftime('%Y-%m-%d')}', Value='{latest_processed_u_value:.4f}', Other value='{previous_processed_u_value:.4f}'")
else:
    print("'df' is EMPTY before writing CSV.")

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "unemployment_rate", "Unemployment rate (%)",x_min, x_max, y_min, y_max)

# Save data

csv_filename = "unemployment_rate.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Unemployment rate (%)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

# Plot vacancy rate

df = pd.DataFrame({"data": v_rate}).dropna()

if not df.empty:
    latest_processed_v_date = df.index.max()
    latest_processed_v_value = df['data'].iloc[-1]
    previous_processed_v_value = df['data'].iloc[-2]
    print(f"Vacancy rate latest processed point for CSV: Date='{latest_processed_v_date.strftime('%Y-%m-%d')}', Value='{latest_processed_v_value:.4f}', Other value='{previous_processed_v_value:.4f}'")
else:
    print("'df' is EMPTY before writing CSV.")

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "vacancy_rate", "Vacancy rate (%)", x_min, x_max, y_min, y_max)

# Save data

csv_filename = "vacancy_rate.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Vacancy rate (%)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

# Immediately after writing, read back and print tail in Python
try:
    df_read_back = pd.read_csv(csv_path_absolute, index_col="Date", parse_dates=True)
    print("Last 5 rows of vacancy_rate.csv as read by Python immediately after write:")
    print(df_read_back.tail(5).to_string())
    latest_read_back_v_date = df_read_back.index.max()
    latest_read_back_v_value = df_read_back["Vacancy rate (%)"].iloc[-1]
    previous_read_back_v_value = df_read_back["Vacancy rate (%)"].iloc[-2]
    print(f"Vacancy rate latest readback point: Date='{latest_read_back_v_date.strftime('%Y-%m-%d')}', Value='{latest_read_back_v_value:.4f}', Other value='{previous_read_back_v_value:.4f}'")

except Exception as e:
    print(f"Error reading back {csv_path_absolute} in Python: {e}")

# Plot labor market tightness

df = pd.DataFrame({"data": tightness}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "labor_market_tightness", "Labor market tightness", x_min, x_max, y_min, y_max, hline=1)

# Save data

csv_filename = "labor_market_tightness.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Labor market tightness"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

# Plot Beveridge curve

df = pd.DataFrame({
    "u": u_rate,
    "v": v_rate
}).dropna()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["u"],
    y=df["v"],
    customdata=df.index.strftime("%b %Y"), 
    mode='markers',
    marker=dict(size=7, color='#59539d'),
    showlegend=False,
    hovertemplate='%{customdata}<br>(%{x:.2f}, %{y:.2f})<extra></extra>'
))

# Add full employment line

max_val = min(df["u"].max(), df["v"].max())

fig.add_trace(go.Scatter(
    x=[0, max_val],
    y=[0, max_val],
    mode='lines',
    line=dict(color='rgba(217, 95, 2, 0.7)', width=1),
    showlegend=False,
    hoverinfo='skip'
))

# Add last observation

last_point = df.iloc[[-1]]

fig.add_trace(go.Scatter(
    x=last_point["u"],
    y=last_point["v"],
    customdata=last_point.index.strftime("%b %Y"),
    mode='markers',
    marker=dict(size=9, color='#e7298a'),
    hovertemplate='%{customdata}<br>(%{x:.2f}, %{y:.2f})<extra></extra>',
    showlegend=False
))

# Adjust layout of graph

fig.update_layout(
    xaxis_title='Unemployment rate (%)',
    yaxis_title='Vacancy rate (%)',
    dragmode=False,
    title_font=dict(size=16),
    font=dict(family="Helvetica", size=16),
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(
        range=[0, df["u"].max() * 1.05],
        title_font=dict(size=16),
        tickfont=dict(size=16),
        showgrid=True,
        showline=True,
        side='bottom',
        mirror=False,
        ticklabelposition="outside",
        ticklabelstandoff=10,
        linecolor='#e9e9e9',
        gridcolor='#e9e9e9'
    ),
    yaxis=dict(
        range=[0, df["v"].max() * 1.05],
        title_font=dict(size=16),
        tickfont=dict(size=16),
        showgrid=True,
        showline=True,
        side='left',
        mirror=False,
        ticklabelposition="outside",
        ticklabelstandoff=10,
        linecolor='#e9e9e9',
        gridcolor='#e9e9e9'
    )
)

# Construct the absolute path for the Beveridge curve HTML
beveridge_curve_html_path = os.path.join(OUTPUT_DIR_ABSOLUTE, "beveridge_curve.html")

fig.write_html(
    beveridge_curve_html_path,
    include_plotlyjs='cdn',
    full_html=False,
    config={
        "displaylogo": False,
        "modeBarButtonsToRemove": [
            "zoomIn2d",
            "zoomOut2d",
            "select2d",
            "lasso2d",
            "autoscale" 
        ],
        "toImageButtonOptions": {
            "format": "png",
            "filename": "beveridge_curve",
            "height": 900,
            "width": 1200,
            "scale": 3
        }
    }
)

print(f"Successfully wrote HTML to: {beveridge_curve_html_path}")


# Plot FERU

df = pd.DataFrame({"data": feru}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "feru", "FERU (%)", x_min, x_max, y_min, y_max)

# Save data

csv_filename = "feru.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["FERU (%)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}") 

# Plot unemployment gap

df = pd.DataFrame({"data": u_gap}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}pp"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = min(0, df["data"].min() * 1.05)
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "unemployment_gap", "Unemployment gap (pp)", x_min, x_max, y_min, y_max, hline=0)

# Save data

csv_filename = "unemployment_gap.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Unemployment gap (pp)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

# Plot recession indicator

df = pd.DataFrame({"data": m}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.2f}pp"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "recession_indicator", "Recession indicator (pp)", x_min, x_max, y_min, y_max, hline=0.29)

# Save data

csv_filename = "recession_indicator.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Recession indicator (pp)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

# Plot recession probability

df = pd.DataFrame({"data": p}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"{last_date}: {last_value:.1f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = 100.5

make_plot(df, "data", title, "recession_probability", "Recession probability", x_min, x_max, y_min, y_max)

# Save data

csv_filename = "recession_probability.csv"
csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
df_out = df.copy()
df_out.columns = ["Recession probability (%)"]
df_out.index.name = "Date"
df_out.to_csv(csv_path_absolute)
print(f"Successfully wrote CSV: {csv_path_absolute}")

print("Script finished.")