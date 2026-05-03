import os
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
else:
    print("FRED_API_KEY environment variable not found.")
fred = Fred(api_key=apikey)
print("FRED object initialized.")

# Set output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
OUTPUT_DIR_ABSOLUTE = os.path.join(REPO_ROOT_DIR, 'static', 'dashboard')
print(f"Ensuring output directory exists: {OUTPUT_DIR_ABSOLUTE}")
os.makedirs(OUTPUT_DIR_ABSOLUTE, exist_ok=True)

# Set shared x-axis start date
DASHBOARD_X_MIN = pd.Timestamp("2005-01-01")

# Convert USREC series into recession start/end intervals
def get_recession_periods(rec_series):
    in_recession = rec_series == 1
    shifts = in_recession.astype(int).diff()

    starts = rec_series.index[shifts == 1]
    ends = rec_series.index[shifts == -1] - pd.offsets.MonthBegin(1)

    # Handle edge cases where recession starts at the beginning or is ongoing
    if in_recession.iloc[0]:
        starts = starts.insert(0, rec_series.index[0])
    if len(ends) < len(starts):
        ends = ends.insert(len(ends), rec_series.index[-1])

    return zip(starts, ends)

# Return a datetime-indexed series, or None if unavailable/empty
def fetch_series_or_none(fred_client, series_id, required=True):
    try:
        series = fred_client.get_series(series_id)
        if series is None or series.empty:
            if required:
                print(f"{series_id} data missing or empty. Dependent graphs will be skipped.")
            else:
                print(f"{series_id} data missing or empty. Continuing without it.")
            return None
        series.index = pd.to_datetime(series.index)
        print(f"{series_id} data fetched successfully: shape = {series.shape}")
        return series
    except Exception as error:
        if required:
            print(f"{series_id} fetch failed: {error}. Dependent graphs will be skipped.")
        else:
            print(f"{series_id} fetch failed: {error}. Continuing without it.")
        return None

def non_empty(series):
    return series is not None and not series.empty

# Log latest raw FRED value for troubleshooting
def log_latest_point(series, series_id):
    latest_date = series.index.max()
    latest_value = series.iloc[-1]
    previous_value = series.iloc[-2]
    print(
        f"{series_id} raw latest point: date = {latest_date.strftime('%Y-%m-%d')}, "
        f"value = {latest_value}, previous value = {previous_value}"
    )

# Log latest processed value for troubleshooting
def log_latest_processed_point(df, series_name):
    latest_processed_date = df.index.max()
    latest_processed_value = df['data'].iloc[-1]
    previous_processed_value = df['data'].iloc[-2]
    print(
        f"{series_name} latest processed point for CSV: date = {latest_processed_date.strftime('%Y-%m-%d')}, "
        f"value = {latest_processed_value:.4f}, previous value = {previous_processed_value:.4f}"
    )

# Save a series to CSV with dashboard naming conventions
def write_dashboard_csv(df, csv_filename, column_name):
    csv_path_absolute = os.path.join(OUTPUT_DIR_ABSOLUTE, csv_filename)
    df_out = df.copy()
    df_out.columns = [column_name]
    df_out.index.name = "Date"
    df_out.to_csv(csv_path_absolute)
    print(f"Successfully wrote CSV: {csv_path_absolute}")

# Build title/axes, write one HTML chart, then write matching CSV
def plot_and_save_series(
    series,
    graph_name,
    y_label,
    csv_column_name,
    title_suffix,
    usrec,
    y_min,
    y_max,
    hline=None,
    precision=2,
    title_precision=2,
    log_processed=False
):
    df = pd.DataFrame({"data": series})

    if log_processed:
        log_latest_processed_point(df, graph_name.replace("_", " ").capitalize())

    last_date = df.index.max().strftime("%B %Y")
    last_value = df["data"].iloc[-1]
    title = f"{last_date}: {last_value:.{title_precision}f}{title_suffix}"

    x_min = DASHBOARD_X_MIN
    x_max = df.index.max()
    y_min_value = y_min(df) if callable(y_min) else y_min
    y_max_value = y_max(df) if callable(y_max) else y_max

    make_plot(
        df,
        "data",
        title,
        graph_name,
        y_label,
        usrec,
        x_min,
        x_max,
        y_min_value,
        y_max_value,
        hline=hline,
        precision=precision
    )

    write_dashboard_csv(
        df,
        f"{graph_name}.csv",
        csv_column_name
    )

# Plot the Beveridge scatter with reference line and highlighted latest point
def plot_beveridge_curve(u_rate, v_rate):
    df = pd.DataFrame({"u": u_rate, "v": v_rate}).dropna()

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

    # Reference 45-degree line marking full employment
    max_val = min(df["u"].max(), df["v"].max())
    fig.add_trace(go.Scatter(
        x=[0, max_val],
        y=[0, max_val],
        mode='lines',
        line=dict(color='rgba(217, 95, 2, 0.7)', width=1),
        showlegend=False,
        hoverinfo='skip'
    ))

    # Highlight the most recent observation
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

    # Save as the embedded HTML fragment used by the site
    beveridge_curve_html_path = os.path.join(OUTPUT_DIR_ABSOLUTE, "beveridge_curve.html")
    fig.write_html(
        beveridge_curve_html_path,
        include_plotlyjs='cdn',
        full_html=False,
        div_id="beveridge_curve",
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

# Plot time-series dashboard chart
def make_plot(df, y_column, title, filename, y_label, usrec, x_min, x_max, y_min, y_max, hline=None, precision=2):
    precision = int(precision)
    hovertemplate = f"%{{x|%b %Y}}<br>%{{y:.{precision}f}}<extra></extra>"
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df[y_column],
        mode='lines',
        line=dict(color='#59539d', width=3),
        hovertemplate=hovertemplate
    ))

    # Shade recession months
    if usrec is not None:
        rec = usrec[(usrec.index >= df.index.min()) & (usrec.index <= df.index.max())]
        for start, end in get_recession_periods(rec):
            fig.add_vrect(
                x0=start, 
                x1=end,
                fillcolor='lightgray', 
                opacity=0.3,
                layer='below', 
                line_width=0
            )
 
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
            range=[x_min, x_max]
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
            range=[y_min, y_max]
        ),
       yaxis_title=dict(
            text=y_label,
            font=dict(size=16)
        ),
        showlegend=False
    )

    html_file_path = os.path.join(OUTPUT_DIR_ABSOLUTE, f"{filename}.html")
    
    fig.write_html(
        html_file_path,
        include_plotlyjs='cdn',
        full_html=False,
        div_id=filename, 
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
usrec = fetch_series_or_none(fred, "USREC", required=False)
u = fetch_series_or_none(fred, "UNEMPLOY")
v = fetch_series_or_none(fred, "JTSJOL")
lf = fetch_series_or_none(fred, "CLF16OV")

# Keep existing published outputs when core data is missing
if not (non_empty(u) and non_empty(v) and non_empty(lf)):
    print("Core input series unavailable. Exiting without generating new files.")
    raise SystemExit(0)

# Print latest points for troubleshooting
log_latest_point(u, "UNEMPLOY")
log_latest_point(v, "JTSJOL")
log_latest_point(lf, "CLF16OV")

# Reshape vacancy data
last_date = v.index.max()
next_date = last_date + pd.offsets.MonthBegin(1)
v_extended = v.reindex(v.index.union([next_date]))
v_shifted = v_extended.shift(1)

# Concatenate data
data = pd.concat([u, v_shifted, lf], axis=1, join='inner')
data.columns = ['u', 'v', 'lf']
data = data.dropna()
if data.empty:
    print("Merged input dataframe is empty after alignment. Exiting without generating new files.")
    raise SystemExit(0)

# Compute simple variables
u_rate = (data['u'] / data['lf']) * 100
v_rate = (data['v'] / data['lf']) * 100
tightness = v_rate / u_rate
feru = (u_rate * v_rate).pow(0.5)
u_gap = u_rate - feru

# Compute Michez-rule variables
# Compute unemployment indicator
u_bar = u_rate.rolling(window=3, min_periods=1).mean()
u_hat = u_bar - u_bar.rolling(window=13, min_periods=1).min()
u_indicator = u_hat.round(2)
# Compute vacancy indicator
v_bar = v_rate.rolling(window=3, min_periods=1).mean()
v_hat = v_bar.rolling(window=13, min_periods=1).max() - v_bar
v_indicator = v_hat.round(2)
# Compute Michez-rule indicator
m = pd.DataFrame({'u_indicator': u_indicator, 'v_indicator': v_indicator}).min(axis=1)
# Compute recession probability
p_exact = (m - 0.29) / (0.81 - 0.29)
p_exact = p_exact.clip(lower=0, upper=1) * 100
p = p_exact.round(1)

# Plot unemployment rate
plot_and_save_series(
    series=u_rate,
    graph_name="unemployment_rate",
    y_label="Unemployment rate (%)",
    csv_column_name="Unemployment rate (%)",
    title_suffix="%",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05,
    log_processed=True
)

# Plot vacancy rate
plot_and_save_series(
    series=v_rate,
    graph_name="vacancy_rate",
    y_label="Vacancy rate (%)",
    csv_column_name="Vacancy rate (%)",
    title_suffix="%",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05,
    log_processed=True
)

# Plot labor market tightness
plot_and_save_series(
    series=tightness,
    graph_name="labor_market_tightness",
    y_label="Labor market tightness",
    csv_column_name="Labor market tightness",
    title_suffix="",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05,
    hline=1
)

# Plot Beveridge curve
plot_beveridge_curve(u_rate, v_rate)

# Plot FERU
plot_and_save_series(
    series=feru,
    graph_name="feru",
    y_label="FERU (%)",
    csv_column_name="FERU (%)",
    title_suffix="%",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05
)

# Plot unemployment gap
plot_and_save_series(
    series=u_gap,
    graph_name="unemployment_gap",
    y_label="Unemployment gap (pp)",
    csv_column_name="Unemployment gap (pp)",
    title_suffix="pp",
    usrec=usrec,
    y_min=lambda frame: min(0, frame["data"].min() * 1.05),
    y_max=lambda frame: frame["data"].max() * 1.05,
    hline=0
)

# Plot unemployment indicator
plot_and_save_series(
    series=u_indicator,
    graph_name="unemployment_indicator",
    y_label="Unemployment indicator (pp)",
    csv_column_name="Unemployment indicator (pp)",
    title_suffix="pp",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05
)

# Plot vacancy indicator
plot_and_save_series(
    series=v_indicator,
    graph_name="vacancy_indicator",
    y_label="Vacancy indicator (pp)",
    csv_column_name="Vacancy indicator (pp)",
    title_suffix="pp",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05
)

# Plot recession indicator
plot_and_save_series(
    series=m,
    graph_name="recession_indicator",
    y_label="Recession indicator (pp)",
    csv_column_name="Recession indicator (pp)",
    title_suffix="pp",
    usrec=usrec,
    y_min=0,
    y_max=lambda frame: frame["data"].max() * 1.05,
    hline=0.29
)

# Plot recession probability
plot_and_save_series(
    series=p,
    graph_name="recession_probability",
    y_label="Recession probability (%)",
    csv_column_name="Recession probability (%)",
    title_suffix="%",
    usrec=usrec,
    y_min=0,
    y_max=100.5,
    precision=1,
    title_precision=1
)

print("Script finished.")