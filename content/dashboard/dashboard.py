# to run from the console:
#  python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt

import os
from datetime import datetime
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
import plotly.graph_objects as go

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# Ensure output directory exists
os.makedirs("../../static/dashboard", exist_ok=True)

# Helper function to fetch recessions
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

def make_plot(df, y_column, title, filename, y_label, x_min=None, x_max=None, y_min=None, y_max=None, hline=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df[y_column],
        mode='lines',
        line=dict(color='#6e55c3', width=3),
        hovertemplate='%{x|%b %Y}<br>%{y:.2f}<extra></extra>'  # <- format to 2 decimal places
    ))

    # Add shaded recession bands
    try:
        rec = fred.get_series("USREC", observation_start=df.index.min(), observation_end=df.index.max())
        rec.index = pd.to_datetime(rec.index)
        for start, end in get_recession_periods(rec):
            fig.add_vrect(
                x0=start,
                x1=end,
                fillcolor='gray',
                opacity=0.3,
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
            line=dict(color='rgba(231, 41, 138, 0.5)', width=1),
            layer='above'
            )

    fig.update_layout(
        title=title,
        title_font=dict(size=15),
        font=dict(family="Helvetica", size=15),
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            side='bottom',
            showline=True, 
            linecolor='lightgray',
            mirror=False,
            ticklabelposition="outside",
            ticklabelstandoff=10,
            gridcolor='lightgray',
            range=[x_min, x_max] if x_min is not None and x_max is not None  else None
        ),
        yaxis=dict(
            showgrid=True, 
            side='left',
            showline=True, 
            linecolor='lightgray',
            mirror=False,
            ticklabelposition="outside",
            ticklabelstandoff=10,
            gridcolor='lightgray',
            range=[y_min, y_max] if y_min is not None and y_max is not None else None
        ),
        yaxis_title=y_label,
        showlegend=False
    )

    fig.write_html(
        f"../../static/dashboard/{filename}",
        include_plotlyjs='cdn',
        full_html=False,
        config={
            "displaylogo": False,
            "modeBarButtonsToRemove": [
            "zoomIn2d",
            "zoomOut2d",
            ],
            "toImageButtonOptions": {
            "format": "png",
            "filename": "dashboard",
            "height": 800,
            "width": 1200,
            "scale": 3  # ↑ export resolution multiplier
            }
        }
    )


# Fetch raw data from FRED
u = fred.get_series("UNEMPLOY")
v = fred.get_series("JTSJOL")
lf = fred.get_series("CLF16OV")

# Ensure datetime index for all series
u.index = pd.to_datetime(u.index)
v.index = pd.to_datetime(v.index)
lf.index = pd.to_datetime(lf.index)


# Align data
# Shift job vacancies forward by 1 month to match unemployment timing
# v_shifted = v.shift(1)

# Extend v's index by 1 month at the end
last_date = v.index.max()
next_date = last_date + pd.offsets.MonthBegin(1)

# Append NaN at the new date
v_extended = v.reindex(v.index.union([next_date]))

# Now shift values forward by 1 month
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

# Compute recession indicator
# Compute 3-month trailing average of unemployment rate
u_bar = u_rate.rolling(window=3, min_periods=1).mean()

# Compute unemployment indicator from equation (1)
u_hat_exact = u_bar - u_bar.rolling(window=13, min_periods=1).min()

# Round to 2 decimal places (basis point precision)
u_hat = u_hat_exact.round(2)

# Compute 3-month trailing average of vacancy rate
v_bar = v_rate.rolling(window=3, min_periods=1).mean()

# Compute vacancy indicator from equation (2)
v_hat_exact = v_bar.rolling(window=13, min_periods=1).max() - v_bar

# Round to 2 decimal places (basis point precision)
v_hat = v_hat_exact.round(2)

# Compute minimum indicator from equation (3)
m = pd.DataFrame({'u_hat': u_hat, 'v_hat': v_hat}).min(axis=1)

# Compute recession probability
# Compute recession probability from equation (6)
p = (m - 0.29) / (0.81 - 0.29)

# Apply dual threshold: clamp values between 0 and 1
p = p.clip(lower=0, upper=1)

# Plot unemployment rate

df = pd.DataFrame({"data": u_rate}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"UNEMPLOYMENT RATE — {last_date} value: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "unemployment.html", "Share of labor force (%)",x_min, x_max, y_min, y_max)

# Plot vacancy rate

df = pd.DataFrame({"data": v_rate}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"VACANCY RATE — {last_date} value: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "vacancy.html", "Share of labor force (%)", x_min, x_max, y_min, y_max)

# Plot labor market tightness

df = pd.DataFrame({"data": tightness}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"LABOR MARKET TIGHTNESS — {last_date} value: {last_value:.2f}"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "tightness.html", "Tightness", x_min, x_max, y_min, y_max, hline=1)

# Plot FERU

df = pd.DataFrame({"data": feru}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"FERU — {last_date} value: {last_value:.2f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "feru.html", "Share of labor force (%)", x_min, x_max, y_min, y_max)

# Plot unemployment gap

df = pd.DataFrame({"data": u_gap}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"UNEMPLOYMENT GAP — {last_date} value: {last_value:.2f}pp"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = min(0, df["data"].min() * 1.05)
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "gap.html", "Share of labor force (pp)", x_min, x_max, y_min, y_max, hline=0)

# Plot minimum indicator

df = pd.DataFrame({"data": m}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1]
title = f"RECESSION INDICATOR — Threshold: 0.29pp— {last_date} value: {last_value:.2f}pp"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = df["data"].max() * 1.05

make_plot(df, "data", title, "indicator.html", "Share of labor force (pp)", x_min, x_max, y_min, y_max, hline=0.29)

# Plot recession probability

df = pd.DataFrame({"data": p}).dropna()

last_date = df.index.max().strftime("%B %Y")
last_value = df["data"].iloc[-1] * 100
title = f"RECESSION PROBABILITY — {last_date} value: {last_value:.0f}%"

x_min = pd.to_datetime("2005-01-01")
x_max = df.index.max()
y_min = 0
y_max = 1.005

make_plot(df, "data", title, "probability.html", "Probability", x_min, x_max, y_min, y_max)