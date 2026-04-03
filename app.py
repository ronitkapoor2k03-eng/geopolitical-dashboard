"""
GEOPOLITICAL INVESTMENT DASHBOARD
Student: Ronit Kapoor
GitHub: ronitkapoor2k03-eng
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# PAGE CONFIGURATION - HIDE DEFAULT HEADER
st.set_page_config(
    page_title="Ronit Kapoor | Geopolitical Investment Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== COMPLETE CSS - FIXES EVERY VISUAL ISSUE ==========
st.markdown("""
<style>
    /* Hide Streamlit default header/top bar completely */
    header[data-testid="stHeader"] {
        display: none !important;
        background-color: #0a0e27 !important;
    }
    
    /* Remove top padding to eliminate white bar */
    .main .block-container {
        padding-top: 1rem !important;
    }
    
    /* Main background - dark navy */
    .stApp {
        background-color: #0a0e27 !important;
    }
    
    /* Force ALL text to be readable */
    html, body, [class*="css"], .stMarkdown, p, div, span, label {
        color: #e2e8f0 !important;
    }
    
    /* Headers - Gold */
    h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #d4af37 !important;
    }
    
    /* SIDEBAR FIX - Dark background, light text */
    [data-testid="stSidebar"] {
        background-color: #0d1128 !important;
        border-right: 1px solid #1a1f3e !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #d4af37 !important;
    }
    
    [data-testid="stSidebar"] label {
        color: #d4af37 !important;
        font-weight: 600 !important;
    }
    
    /* Sidebar select box */
    .stSelectbox div[data-baseweb="select"] div {
        background-color: #1a1f3e !important;
        color: #e2e8f0 !important;
        border: 1px solid #d4af37 !important;
    }
    
    .stSelectbox div[data-baseweb="select"] div:hover {
        border-color: #d4af37 !important;
    }
    
    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: #1a1f3e !important;
        border-radius: 12px !important;
        padding: 15px !important;
        border-left: 4px solid #d4af37 !important;
    }
    
    div[data-testid="stMetric"] label {
        color: #94a3b8 !important;
        font-size: 0.85rem !important;
    }
    
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #d4af37 !important;
        font-size: 1.8rem !important;
        font-weight: bold !important;
    }
    
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        font-size: 0.9rem !important;
    }
    
    /* Delta colors - green for positive, red for negative */
    .delta-positive {
        color: #10b981 !important;
    }
    .delta-negative {
        color: #ef4444 !important;
    }
    
    /* Info boxes */
    .stAlert {
        background-color: #1a1f3e !important;
        border-left: 3px solid #d4af37 !important;
    }
    
    .stAlert p {
        color: #e2e8f0 !important;
    }
    
    /* Dataframe */
    .stDataFrame {
        background-color: #0a0e27 !important;
    }
    .dataframe {
        color: #e2e8f0 !important;
        background-color: #0a0e27 !important;
    }
    .dataframe th {
        background-color: #1a1f3e !important;
        color: #d4af37 !important;
    }
    .dataframe td {
        background-color: #0a0e27 !important;
        color: #e2e8f0 !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #d4af37 !important;
        background-color: #1a1f3e !important;
        border-radius: 8px !important;
    }
    .streamlit-expanderContent {
        background-color: #0a0e27 !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #d4af37 !important;
        color: #0a0e27 !important;
        font-weight: bold !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdown"] p {
        color: #e2e8f0 !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        border-bottom-color: #d4af37 !important;
    }
    
    /* Any remaining white elements */
    .element-container, .row-widget, .stHorizontalBlock {
        background-color: transparent !important;
    }
    
    /* Fix for any white backgrounds */
    div[style*="background-color: rgb(255, 255, 255)"] {
        background-color: #0a0e27 !important;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("## INVESTMENT CONTROLS")
    st.markdown("---")
    
    scenario = st.selectbox(
        "CONFLICT SCENARIO",
        ["Short War (Baseline Thesis)", "Prolonged Conflict", "Rapid De-escalation"],
        help="Select scenario to update all projections"
    )
    
    st.markdown("---")
    st.markdown("### ANALYST INFORMATION")
    st.markdown(f"**Name:** Ronit Kapoor")
    st.markdown(f"**GitHub:** ronitkapoor2k03-eng")
    st.markdown(f"**Analysis Date:** {datetime.now().strftime('%d %B %Y')}")
    
    st.markdown("---")
    st.markdown("### DATA SOURCES")
    st.markdown("""
    - EIA Weekly Petroleum Report
    - IEA Monthly Oil Market Report
    - Federal Reserve Economic Data
    - Bloomberg Terminal Projections
    - US Department of Defense
    """)

# MAIN HEADER
st.markdown("""
<h1 style="color: #d4af37; font-size: 2.5rem; font-weight: 700; text-align: center; padding: 1rem 0 0.5rem 0; margin: 0;">
THE PERSIAN GULF SHOCK
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="color: #94a3b8; font-size: 1.1rem; text-align: center; margin-bottom: 2rem;">
Investment Analysis: US-Israel-Iran War Impact on Global Financial Markets | 3-6 Month Forecast Horizon
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# SET METRIC VALUES BASED ON SCENARIO
if scenario == "Short War (Baseline Thesis)":
    oil_price = "$118/bbl"
    oil_delta = "+59.5%"
    oil_delta_color = "normal"
    sp500 = "4,820"
    sp500_delta = "-9.2%"
    sp500_delta_color = "inverse"
    gold = "$5,400/oz"
    gold_delta = "+18.5%"
    gold_delta_color = "normal"
    vix = "28.4"
    vix_delta = "+61.4%"
    vix_delta_color = "inverse"
elif scenario == "Prolonged Conflict":
    oil_price = "$148/bbl"
    oil_delta = "+100%"
    oil_delta_color = "normal"
    sp500 = "4,200"
    sp500_delta = "-20.8%"
    sp500_delta_color = "inverse"
    gold = "$5,800/oz"
    gold_delta = "+27.3%"
    gold_delta_color = "normal"
    vix = "42.0"
    vix_delta = "+138%"
    vix_delta_color = "inverse"
else:
    oil_price = "$90/bbl"
    oil_delta = "+21.6%"
    oil_delta_color = "normal"
    sp500 = "5,400"
    sp500_delta = "+1.7%"
    sp500_delta_color = "normal"
    gold = "$5,100/oz"
    gold_delta = "+11.9%"
    gold_delta_color = "normal"
    vix = "18.5"
    vix_delta = "+5.1%"
    vix_delta_color = "inverse"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="BRENT CRUDE (Projected Spot)",
        value=oil_price,
        delta=oil_delta,
        delta_color=oil_delta_color
    )

with col2:
    st.metric(
        label="S&P 500 (3-Month Target)",
        value=sp500,
        delta=sp500_delta,
        delta_color=sp500_delta_color
    )

with col3:
    st.metric(
        label="GOLD (6-Month Target)",
        value=gold,
        delta=gold_delta,
        delta_color=gold_delta_color
    )

with col4:
    st.metric(
        label="VIX FEAR INDEX",
        value=vix,
        delta=vix_delta,
        delta_color=vix_delta_color
    )

st.markdown("---")

# ========== OIL PRICE CHART ==========
st.markdown("## ENERGY SHOCK ANALYSIS")
st.markdown("The Strait of Hormuz blockade has reduced oil transit traffic to less than 20 percent of normal capacity.")

months = ['Apr 2026', 'May 2026', 'Jun 2026', 'Jul 2026', 'Aug 2026', 'Sep 2026']

if scenario == "Short War (Baseline Thesis)":
    oil_prices = [95, 112, 118, 108, 94, 82]
    lower_band = [88, 104, 110, 100, 86, 75]
    upper_band = [102, 120, 126, 116, 102, 89]
    scenario_title = "SHORT WAR RESOLUTION BY Q3 2026"
    line_color = "#d4af37"
elif scenario == "Prolonged Conflict":
    oil_prices = [105, 128, 145, 148, 140, 132]
    lower_band = [98, 118, 135, 138, 130, 122]
    upper_band = [112, 138, 155, 158, 150, 142]
    scenario_title = "EXTENDED BLOCKADE - STAGFLATION RISK"
    line_color = "#ef4444"
else:
    oil_prices = [90, 94, 90, 85, 80, 76]
    lower_band = [84, 88, 84, 79, 74, 70]
    upper_band = [96, 100, 96, 91, 86, 82]
    scenario_title = "RAPID DIPLOMATIC RESOLUTION"
    line_color = "#10b981"

fig_oil = go.Figure()
fig_oil.add_trace(go.Scatter(
    x=months, y=oil_prices, mode='lines+markers',
    name='Brent Crude', line=dict(color=line_color, width=3),
    marker=dict(size=10, color=line_color, symbol='diamond')
))
fig_oil.add_trace(go.Scatter(
    x=months + months[::-1], y=upper_band + lower_band[::-1],
    fill='toself', fillcolor=f'rgba(100,100,100,0.15)',
    line=dict(color='rgba(255,255,255,0)'), hoverinfo="skip", name='Confidence Band'
))
fig_oil.add_hline(y=74, line_dash="dash", line_color="#ef4444", 
                  annotation_text="Pre-Conflict: $74/bbl", annotation_position="bottom right")
fig_oil.update_layout(
    title=f'OIL PRICE: {scenario_title}', title_font=dict(size=16, color='#d4af37'),
    xaxis_title='Month', yaxis_title='USD per Barrel',
    plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27',
    font=dict(color='#e2e8f0'), height=450,
    xaxis=dict(gridcolor='#1a1f3e'), yaxis=dict(gridcolor='#1a1f3e')
)
st.plotly_chart(fig_oil, use_container_width=True)
st.info(f"Analyst Note: {scenario} - Oil peaks at ${max(oil_prices)}/bbl")

st.markdown("---")

# ========== SECTOR CHART ==========
st.markdown("## SECTOR PERFORMANCE PROJECTION")

if scenario == "Short War (Baseline Thesis)":
    sector_data = {'Sector': ['Energy', 'Defense', 'Utilities', 'Consumer Disc', 'Semis', 'Healthcare', 'Financials', 'Tech'],
                   'Return (%)': [58, 28, -6, -32, -22, 6, -12, -18]}
    color_scheme = 'RdYlGn'
elif scenario == "Prolonged Conflict":
    sector_data = {'Sector': ['Energy', 'Defense', 'Utilities', 'Consumer Disc', 'Semis', 'Healthcare', 'Financials', 'Tech'],
                   'Return (%)': [82, 42, -12, -48, -38, -4, -25, -32]}
    color_scheme = 'Reds'
else:
    sector_data = {'Sector': ['Energy', 'Defense', 'Utilities', 'Consumer Disc', 'Semis', 'Healthcare', 'Financials', 'Tech'],
                   'Return (%)': [22, 12, 3, 18, 28, 8, 10, 15]}
    color_scheme = 'Greens'

sector_df = pd.DataFrame(sector_data)
fig_sectors = px.bar(sector_df, x='Return (%)', y='Sector', orientation='h',
                      color='Return (%)', color_continuous_scale=color_scheme,
                      title=f'SECTOR RETURNS: {scenario.upper()}', text='Return (%)')
fig_sectors.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_sectors.update_layout(plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27',
                           font=dict(color='#e2e8f0'), height=450,
                           xaxis=dict(gridcolor='#1a1f3e'), yaxis=dict(gridcolor='#1a1f3e'))
st.plotly_chart(fig_sectors, use_container_width=True)

with st.expander("VIEW SECTOR JUSTIFICATION"):
    st.markdown("""
    | Sector | Why | Projected Return |
    |:---|:---|:---|
    | Energy | Hormuz blockade supply shock | 58-82% |
    | Defense | $200bn supplemental budget | 28-42% |
    | Consumer Disc. | Gas prices destroy disposable income | -32% to -48% |
    """)

st.markdown("---")

# ========== TIMELINE ==========
st.markdown("## STRATEGIC INVESTMENT TIMELINE")

phases = ['PHASE 1: SCRAMBLE', 'PHASE 2: CAPITULATION', 'PHASE 3: RE-PIVOT']
starts = [0, 45, 100]
ends = [45, 100, 180]
colors_phase = ['#ef4444', '#f59e0b', '#10b981']

fig_time = go.Figure()
for i, phase in enumerate(phases):
    fig_time.add_trace(go.Scatter(x=[starts[i], ends[i]], y=[phase, phase],
                                   mode='lines+markers', line=dict(width=35, color=colors_phase[i]),
                                   name=phase))
fig_time.update_layout(title='INVESTMENT TIMELINE - ENTRY AND EXIT POINTS',
                        title_font=dict(color='#d4af37'), plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27',
                        font=dict(color='#e2e8f0'), height=350,
                        xaxis=dict(gridcolor='#1a1f3e', tickmode='linear', tick0=0, dtick=30))
st.plotly_chart(fig_time, use_container_width=True)

st.markdown("---")

# ========== GEOGRAPHIC IMPACT ==========
st.markdown("## REGIONAL ECONOMIC IMPACT")

geo_df = pd.DataFrame({
    'Region': ['US', 'EU', 'Japan/Korea', 'India', 'China', 'Saudi/UAE', 'UK'],
    'GDP Revision': [-0.8, -1.4, -1.2, -1.8, -1.0, 1.8, -0.9],
    'Currency': ['Bullish', 'Bearish', 'Bearish', 'Bearish', 'Stable', 'Pegged', 'Bearish']
})

fig_geo = px.bar(geo_df, x='Region', y='GDP Revision', color='GDP Revision',
                  color_continuous_scale='RdYlGn_r', title='GDP FORECAST REVISIONS',
                  text='GDP Revision')
fig_geo.update_traces(texttemplate='%{text:.1f} pp', textposition='outside')
fig_geo.update_layout(plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27',
                       font=dict(color='#e2e8f0'), height=400)
st.plotly_chart(fig_geo, use_container_width=True)

st.markdown("---")

# ========== INVESTMENT THESIS ==========
st.markdown("## INVESTMENT THESIS: SHORT, SHARP, SHOCK")

col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("### CORE POSITIONING")
    st.markdown("""
    **HOLD GOLD** - Target $5,400/oz by Q4 2026
    
    **BUY DEFENSE** - 5-year replenishment cycle
    
    **AVOID EU AIRLINES** - Unhedged fuel exposure
    """)

with col_t2:
    st.markdown("### RISKS")
    st.markdown("""
    | Risk | Probability |
    |:---|:---|
    | Hormuz blocked through Q3 | 25% |
    | Iran proxy escalation | 35% |
    | Fed emergency hike | 10% |
    """)

st.markdown("---")

# ========== FORECAST ==========
st.markdown("## FORECAST SUMMARY")

forecast_df = pd.DataFrame({
    'Asset': ['Brent Crude', 'S&P 500', 'Gold', 'VIX'],
    'Current': [oil_price, sp500, gold, vix],
    '3-Month': ['$108-112', '4,850-4,950', '$5,250-5,300', '22-25'],
    '6-Month': ['$82-94', '5,100-5,250', '$5,350-5,450', '16-19']
})
st.dataframe(forecast_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <p style="color: #94a3b8;">GEOPOLITICAL INVESTMENT DASHBOARD | ANALYST: RONIT KAPOOR</p>
    <p style="color: #94a3b8; font-size: 0.8rem;">Data: EIA, IEA, FRED, Bloomberg | April 3, 2026</p>
</div>
""", unsafe_allow_html=True)
