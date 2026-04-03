"""
GEOPOLITICAL INVESTMENT DASHBOARD
Student: Ronit Kapoor
GitHub: ronitkapoor2k03-eng
Course: Financial Investment Analysis
Topic: US-Israel-Iran War Impact on Global Financial Markets
Date: April 2026
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import base64

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Ronit Kapoor | Geopolitical Investment Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS FOR PROFESSIONAL DARK THEME
st.markdown("""
<style>
    .stApp {
        background-color: #0a0e27;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #d4af37;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid #d4af37;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #8892b0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #1a1f3e;
        border-radius: 10px;
        padding: 1rem;
        border-left: 4px solid #d4af37;
    }
    .thesis-box {
        background-color: #1a1f3e;
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #d4af37;
    }
    .risk-box {
        background-color: #2a1a1a;
        border-radius: 10px;
        padding: 1.5rem;
        border-left: 4px solid #dc2626;
    }
    h1, h2, h3 {
        color: #d4af37 !important;
    }
    .stMarkdown {
        color: #ccd6f6;
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
        help="Select scenario to update all projections dynamically"
    )
    
    st.markdown("---")
    st.markdown("### ANALYST INFORMATION")
    st.markdown(f"**Name:** Ronit Kapoor")
    st.markdown(f"**GitHub:** ronitkapoor2k03-eng")
    st.markdown(f"**Analysis Date:** {datetime.now().strftime('%d %B %Y')}")
    st.markdown(f"**Report Status:** Current as of April 2026")
    
    st.markdown("---")
    st.markdown("### DATA SOURCES")
    st.markdown("""
    - EIA Weekly Petroleum Report
    - IEA Monthly Oil Market Report
    - Federal Reserve Economic Data
    - Bloomberg Terminal (Projections)
    - US Department of Defense Briefings
    """)
    
    st.markdown("---")
    download_report = st.button("DOWNLOAD FULL INVESTMENT REPORT", use_container_width=True)

# MAIN HEADER
st.markdown('<div class="main-header">THE PERSIAN GULF SHOCK</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Investment Analysis: US-Israel-Iran War Impact on Global Financial Markets | 3-6 Month Forecast Horizon</div>', unsafe_allow_html=True)
st.markdown("---")

# KEY METRICS ROW
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="BRENT CRUDE (Projected Spot)",
        value="$118/bbl",
        delta="+59.5% vs Pre-Conflict",
        delta_color="inverse"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="S&P 500 (3-Month Target)",
        value="4,820",
        delta="-9.2%",
        delta_color="inverse"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="GOLD (6-Month Target)",
        value="$5,400/oz",
        delta="+18.5%",
        delta_color="normal"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="VIX FEAR INDEX",
        value="28.4",
        delta="+61.4%",
        delta_color="inverse"
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# SECTION 1: OIL PRICE TRAJECTORY
st.markdown("## ENERGY SHOCK ANALYSIS")
st.markdown("The Strait of Hormuz blockade has reduced oil transit traffic to less than 20% of normal capacity. Iran's naval operations have effectively closed the world's most critical energy chokepoint.")

# Define scenarios
months = ['Apr 2026', 'May 2026', 'Jun 2026', 'Jul 2026', 'Aug 2026', 'Sep 2026']
month_nums = list(range(6))

if scenario == "Short War (Baseline Thesis)":
    oil_prices = [95, 112, 118, 108, 94, 82]
    lower_band = [88, 104, 110, 100, 86, 75]
    upper_band = [102, 120, 126, 116, 102, 89]
    scenario_title = "SHORT WAR RESOLUTION BY Q3 2026"
elif scenario == "Prolonged Conflict":
    oil_prices = [105, 128, 145, 148, 140, 132]
    lower_band = [98, 118, 135, 138, 130, 122]
    upper_band = [112, 138, 155, 158, 150, 142]
    scenario_title = "EXTENDED BLOCKADE - STAGFLATION RISK"
else:
    oil_prices = [90, 94, 90, 85, 80, 76]
    lower_band = [84, 88, 84, 79, 74, 70]
    upper_band = [96, 100, 96, 91, 86, 82]
    scenario_title = "RAPID DIPLOMATIC RESOLUTION"

fig_oil = go.Figure()

fig_oil.add_trace(go.Scatter(
    x=months,
    y=oil_prices,
    mode='lines+markers',
    name='Brent Crude Forecast',
    line=dict(color='#d4af37', width=3),
    marker=dict(size=10, color='#d4af37', symbol='diamond')
))

fig_oil.add_trace(go.Scatter(
    x=months + months[::-1],
    y=upper_band + lower_band[::-1],
    fill='toself',
    fillcolor='rgba(212, 175, 55, 0.15)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    name='Confidence Band (75%)'
))

fig_oil.add_hline(y=74, line_dash="dash", line_color="red", annotation_text="Pre-Conflict Baseline: $74/bbl", annotation_position="bottom right")

fig_oil.update_layout(
    title=f'OIL PRICE TRAJECTORY: {scenario_title}',
    title_font=dict(size=16, color='#d4af37'),
    xaxis_title='Month',
    yaxis_title='USD per Barrel',
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    font=dict(color='#ccd6f6'),
    xaxis=dict(gridcolor='#1a1f3e', showgrid=True),
    yaxis=dict(gridcolor='#1a1f3e', showgrid=True),
    hovermode='x unified',
    height=500
)

st.plotly_chart(fig_oil, use_container_width=True)

st.info("ANALYST NOTE: The forward curve shows backwardation in Short War scenario, indicating market expects resolution within 90 days. Prolonged conflict shows contango, signaling sustained supply concerns.")

st.markdown("---")

# SECTION 2: SECTOR PERFORMANCE
st.markdown("## SECTOR PERFORMANCE PROJECTION")
st.markdown("3 to 6 month forward returns based on conflict phase analysis and historical recovery patterns.")

sector_data = {
    'Sector': ['Energy (XLE)', 'Aerospace & Defense (ITA)', 'Utilities (XLU)', 'Consumer Discretionary (XLY)', 'Semiconductors (SOXX)', 'Healthcare (XLV)', 'Financials (XLF)', 'Technology (XLK)'],
    'Short_War': [58, 28, -6, -32, -22, 6, -12, -18],
    'Prolonged': [82, 42, -12, -48, -38, -4, -25, -32],
    'De_escalation': [22, 12, 3, 18, 28, 8, 10, 15]
}

sector_df = pd.DataFrame(sector_data)

if scenario == "Short War (Baseline Thesis)":
    returns = sector_df['Short_War']
    color_scale = 'RdYlGn'
elif scenario == "Prolonged Conflict":
    returns = sector_df['Prolonged']
    color_scale = 'Reds'
else:
    returns = sector_df['De_escalation']
    color_scale = 'Viridis'

fig_sectors = px.bar(
    sector_df,
    x=returns,
    y='Sector',
    orientation='h',
    color=returns,
    color_continuous_scale=color_scale,
    title=f'SECTOR RETURNS BY SCENARIO: {scenario.upper()}',
    labels={'x': 'Projected Return (%)', 'y': ''},
    text=returns
)

fig_sectors.update_traces(
    texttemplate='%{text:.1f}%',
    textposition='outside',
    marker=dict(line=dict(width=0))
)

fig_sectors.update_layout(
    title_font=dict(size=16, color='#d4af37'),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    font=dict(color='#ccd6f6'),
    xaxis=dict(gridcolor='#1a1f3e', showgrid=True),
    yaxis=dict(gridcolor='#1a1f3e', showgrid=True),
    height=500,
    coloraxis_colorbar=dict(title="Return %", title_font=dict(color='#ccd6f6'), tickfont=dict(color='#ccd6f6'))
)

st.plotly_chart(fig_sectors, use_container_width=True)

# Sector justification table
with st.expander("VIEW SECTOR JUSTIFICATION - WHY, WHAT, AND HOW"):
    st.markdown("""
    | Sector | Why | What | How |
    |:---|:---|:---|:---|
    | Energy (XLE) | Supply shock from Hormuz blockade | 58-82% projected returns | Margin expansion at $100+ oil |
    | Aerospace & Defense (ITA) | US supplemental budget of $200bn for munitions replenishment | 28-42% returns | Multi-year procurement cycle begins |
    | Consumer Discretionary (XLY) | Gas prices at $4.50+ destroy disposable income | -32% to -48% returns | Walmart effect - trade down to staples |
    | Semiconductors (SOXX) | Energy costs for fabs increase 40%; Qatar gas disruption | -22% to -38% returns | TSMC and Samsung margin compression |
    """)

st.markdown("---")

# SECTION 3: CONFLICT TIMELINE
st.markdown("## STRATEGIC INVESTMENT TIMELINE")
st.markdown("Phased approach to capital allocation based on conflict progression.")

phases = ['PHASE 1: THE SCRAMBLE', 'PHASE 2: CAPITULATION', 'PHASE 3: RE-PIVOT']
phase_starts = [0, 45, 100]
phase_ends = [45, 100, 180]
phase_colors = ['#dc2626', '#f59e0b', '#10b981']
phase_actions = [
    'Underweight international equities (EWJ, EEM). Overweight Energy, Defense, USD cash. VIX >25.',
    'Take profits on Energy. Aggressively buy oversold European Luxury (LVMH) and Asian Industrials (Samsung).',
    'Fed pivot as energy prices retreat. Rotate into Growth/Tech. AI productivity thesis re-emerges.'
]
phase_oil_targets = ['$95 - $120/bbl', '$85 - $95/bbl', '$75 - $85/bbl']

fig_timeline = go.Figure()

for i, phase in enumerate(phases):
    fig_timeline.add_trace(go.Scatter(
        x=[phase_starts[i], phase_ends[i]],
        y=[phase, phase],
        mode='lines+markers',
        line=dict(width=35, color=phase_colors[i]),
        marker=dict(size=12, symbol='arrow', angleref='previous'),
        name=phase,
        hovertemplate=f'<b>{phase}</b><br>Duration: {phase_ends[i]-phase_starts[i]} days<br>Oil: {phase_oil_targets[i]}<br>{phase_actions[i]}<extra></extra>'
    ))

fig_timeline.update_layout(
    title='CONFLICT PHASE TIMELINE WITH ENTRY AND EXIT POINTS',
    title_font=dict(size=16, color='#d4af37'),
    xaxis_title='Days from Current Date (April 3, 2026)',
    yaxis_title='Investment Phase',
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    font=dict(color='#ccd6f6'),
    xaxis=dict(gridcolor='#1a1f3e', tickmode='linear', tick0=0, dtick=30, range=[-5, 185]),
    yaxis=dict(gridcolor='#1a1f3e'),
    height=350,
    showlegend=True,
    legend=dict(font=dict(color='#ccd6f6'), bgcolor='#0a0e27')
)

st.plotly_chart(fig_timeline, use_container_width=True)

st.markdown("---")

# SECTION 4: GEOGRAPHIC IMPACT
st.markdown("## REGIONAL ECONOMIC IMPACT MATRIX")
st.markdown("Divergent outcomes based on energy exposure, fiscal capacity, and trade relationships.")

geo_data = {
    'Region': ['United States', 'European Union', 'Japan / South Korea', 'India', 'China', 'Saudi Arabia / UAE', 'United Kingdom'],
    'GDP Revision (pp)': [-0.8, -1.4, -1.2, -1.8, -1.0, 1.8, -0.9],
    'Currency Outlook': ['Bullish (DXY)', 'Bearish (EUR)', 'Bearish (JPY)', 'Bearish (INR)', 'Stable (CNY Pegged)', 'Pegged to USD', 'Bearish (GBP)'],
    'Inflation Shock': ['Moderate', 'Severe', 'Severe', 'Extreme', 'Moderate', 'Low', 'Severe'],
    'Policy Response': ['SPR Release + Rate Holds', 'Emergency Energy Subsidies', 'FX Intervention', 'Subsidies + Black Market', 'Strategic Reserve Draw', 'Production Increase', 'Windfall Tax']
}

geo_df = pd.DataFrame(geo_data)

# Color coding for GDP revision
fig_geo = px.bar(
    geo_df,
    x='Region',
    y='GDP Revision (pp)',
    color='GDP Revision (pp)',
    color_continuous_scale='RdYlGn_r',
    title='GDP FORECAST REVISIONS BY REGION (Percentage Points)',
    text='GDP Revision (pp)'
)

fig_geo.update_traces(texttemplate='%{text:.1f} pp', textposition='outside')
fig_geo.update_layout(
    title_font=dict(size=16, color='#d4af37'),
    plot_bgcolor='#0a0e27',
    paper_bgcolor='#0a0e27',
    font=dict(color='#ccd6f6'),
    xaxis=dict(gridcolor='#1a1f3e', tickangle=45),
    yaxis=dict(gridcolor='#1a1f3e'),
    height=450,
    coloraxis_colorbar=dict(title="GDP Change (pp)", title_font=dict(color='#ccd6f6'))
)

st.plotly_chart(fig_geo, use_container_width=True)

st.dataframe(geo_df, use_container_width=True, hide_index=True)

st.markdown("---")

# SECTION 5: VALUATION AND RISK METRICS
st.markdown("## VALUATION & RISK DASHBOARD")
st.markdown("Quantitative metrics supporting the investment thesis.")

col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    fig_gauge1 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=48,
        title={"text": "US RECESSION PROBABILITY (6-Month)", "font": {"color": "#d4af37"}},
        delta={"reference": 32, "increasing": {"color": "red"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#ccd6f6"},
            "bar": {"color": "#d4af37"},
            "bgcolor": "#1a1f3e",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 30], "color": "#0a2e1a"},
                {"range": [30, 60], "color": "#3d2e1a"},
                {"range": [60, 100], "color": "#3d1a1a"}
            ],
            "threshold": {"line": {"color": "red", "width": 2}, "thickness": 0.75, "value": 48}
        }
    ))
    fig_gauge1.update_layout(plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27', height=300, font=dict(color='#ccd6f6'))
    st.plotly_chart(fig_gauge1, use_container_width=True)

with col_r2:
    fig_gauge2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=5.2,
        title={"text": "CPI PEAK FORECAST (%)", "font": {"color": "#d4af37"}},
        gauge={
            "axis": {"range": [0, 12], "tickcolor": "#ccd6f6"},
            "bar": {"color": "#d4af37"},
            "bgcolor": "#1a1f3e",
            "steps": [
                {"range": [0, 4], "color": "#0a2e1a"},
                {"range": [4, 7], "color": "#3d2e1a"},
                {"range": [7, 12], "color": "#3d1a1a"}
            ]
        }
    ))
    fig_gauge2.update_layout(plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27', height=300, font=dict(color='#ccd6f6'))
    st.plotly_chart(fig_gauge2, use_container_width=True)

with col_r3:
    fig_gauge3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=39,
        title={"text": "US DEBT (TRILLIONS USD)", "font": {"color": "#d4af37"}},
        gauge={
            "axis": {"range": [0, 50], "tickcolor": "#ccd6f6"},
            "bar": {"color": "#d4af37"},
            "bgcolor": "#1a1f3e",
            "steps": [
                {"range": [0, 35], "color": "#0a2e1a"},
                {"range": [35, 45], "color": "#3d2e1a"},
                {"range": [45, 50], "color": "#3d1a1a"}
            ]
        }
    ))
    fig_gauge3.update_layout(plot_bgcolor='#0a0e27', paper_bgcolor='#0a0e27', height=300, font=dict(color='#ccd6f6'))
    st.plotly_chart(fig_gauge3, use_container_width=True)

st.markdown("---")

# SECTION 6: INVESTMENT THESIS
st.markdown("## INVESTMENT THESIS: THE SHORT, SHARP, SHOCK HYPOTHESIS")
st.markdown('<div class="thesis-box">', unsafe_allow_html=True)

col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("### CORE POSITIONING")
    st.markdown("""
    **1. HOLD PHYSICAL GOLD**
    - Current price: $5,129/oz
    - Target (Q4 2026): $5,400/oz
    - Rationale: Margin call selling is temporary; fiat debasement via war spending drives reversion
    
    **2. BUY DEFENSE DIP**
    - Primary beneficiaries: Lockheed Martin (LMT), RTX Corporation
    - Catalyst: $200bn supplemental defense budget
    - Time horizon: 5-year replenishment cycle
    
    **3. AVOID EUROPEAN AIRLINES**
    - Lufthansa (LHA), IAG (ICAGY)
    - Risk: Unhedged fuel exposure + demand destruction
    - Outlook: Government bailouts required
    """)

with col_t2:
    st.markdown("### RISKS TO THESIS")
    st.markdown("""
    | Risk Factor | Probability | Impact |
    |:---|:---|:---|
    | Hormuz Blockade through Q3 2026 | 25% | Severe - Stagflation |
    | Iran Proxy Escalation (Hezbollah) | 35% | High - Regional war |
    | US Fiscal Gridlock | 15% | Medium - Delayed stimulus |
    | Fed Emergency Hike | 10% | High - Equity selloff |
    """)
    
    st.markdown("### WORST-CASE SCENARIO")
    st.markdown("If Strait of Hormuz remains blocked through September 2026, enter 1970s-style stagflation. Commodities become only store of value. Equities de-rate by 30%.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# SECTION 7: FORECAST SUMMARY TABLE
st.markdown("## 3 TO 6 MONTH FORECAST SUMMARY")
st.markdown("Specific projections with catalysts and confidence levels.")

forecast_data = {
    'Asset / Indicator': ['Brent Crude (Sep 2026)', 'S&P 500 (Sep 2026)', 'Gold (Sep 2026)', 'USD Index (DXY)', '10Y Treasury Yield', 'VIX (Sep 2026)'],
    'Current Value': ['$118', '5,310', '$5,129', '105.2', '4.35%', '28.4'],
    '3-Month Forecast': ['$108-$112', '4,850-4,950', '$5,250-$5,300', '106-108', '4.10%-4.30%', '22-25'],
    '6-Month Forecast': ['$82-$94', '5,100-5,250', '$5,350-$5,450', '103-105', '3.80%-4.00%', '16-19'],
    'Catalyst': ['Peace negotiations', 'Fed pivot signal', 'Rate cut expectations', 'Risk-off flows', 'Recession pricing', 'Resolution pricing']
}

forecast_df = pd.DataFrame(forecast_data)
st.dataframe(forecast_df, use_container_width=True, hide_index=True)

st.markdown("---")

# FOOTER
st.markdown("""
<div style="text-align: center; padding: 2rem 0; border-top: 1px solid #1a1f3e; margin-top: 2rem;">
    <p style="color: #8892b0;">GEOPOLITICAL INVESTMENT DASHBOARD | ANALYST: RONIT KAPOOR</p>
    <p style="color: #8892b0; font-size: 0.8rem;">Data sourced from EIA, IEA, FRED, Bloomberg Terminal Projections | Analysis Date: April 3, 2026</p>
    <p style="color: #8892b0; font-size: 0.8rem;">This dashboard represents independent investment analysis for academic purposes.</p>
</div>
""", unsafe_allow_html=True)
