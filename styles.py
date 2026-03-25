import streamlit as st

THEMES = {
    "dark": {
        "bg": "#0b0e14", "bg_secondary": "#0f1318", "card": "#161b22", "card_hover": "#1c2330",
        "surface": "#1f2937", "text": "#f0f4f8", "text_secondary": "#8b949e", "text_muted": "#484f58",
        "border": "#30363d", "border_subtle": "#21262d", "accent": "#00ff88", "accent_dim": "rgba(0,255,136,0.1)",
        "accent_glow": "rgba(0,255,136,0.25)", "critical": "#ff4b4b", "critical_dim": "rgba(255,75,75,0.08)",
        "warning": "#ffa500", "warning_dim": "rgba(255,165,0,0.08)", "info": "#58a6ff", "info_dim": "rgba(88,166,255,0.08)",
        "success": "#3fb950", "success_dim": "rgba(63,185,80,0.08)", "input_bg": "#0d1117",
        "shadow_card": "0 2px 12px rgba(0,0,0,0.35)",
    },
    "light": {
        "bg": "#f5f7fa", "bg_secondary": "#eef0f5", "card": "#ffffff", "card_hover": "#f8f9fc",
        "surface": "#f0f2f7", "text": "#0f172a", "text_secondary": "#475569", "text_muted": "#94a3b8",
        "border": "#e2e8f0", "border_subtle": "#f1f5f9", "accent": "#0070f3", "accent_dim": "rgba(0,112,243,0.08)",
        "accent_glow": "rgba(0,112,243,0.18)", "critical": "#dc2626", "critical_dim": "rgba(220,38,38,0.06)",
        "warning": "#d97706", "warning_dim": "rgba(217,119,6,0.06)", "info": "#2563eb", "info_dim": "rgba(37,99,235,0.06)",
        "success": "#16a34a", "success_dim": "rgba(22,163,74,0.06)", "input_bg": "#f8fafc",
        "shadow_card": "0 2px 12px rgba(15,23,42,0.06)",
    },
}

def get_theme() -> dict:
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    return THEMES[st.session_state.theme]

def apply_custom_css():
    t = get_theme()
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    [data-testid="stMain"] {{ background-color: {t['bg']} !important; }}
    
    [data-testid="stMain"] h1, [data-testid="stMain"] h2, [data-testid="stMain"] h3, 
    [data-testid="stMain"] p, [data-testid="stMain"] span, [data-testid="stMain"] div {{ color: {t['text']}; }}
    
    .kpi-box {{
        background-color: {t['card']}; border: 1px solid {t['border']}; border-radius: 12px;
        padding: 1.25rem; box-shadow: {t['shadow_card']}; transition: all 0.2s ease;
    }}
    .kpi-box:hover {{ border-color: {t['accent']}; transform: translateY(-2px); }}
    .kpi-label {{ font-size: 0.82rem; font-weight: 600; text-transform: uppercase; color: {t['text_secondary']} !important; }}
    .kpi-value {{ font-size: 2.2rem; font-weight: 700; line-height: 1.2; }}
    
    [data-testid="stPlotlyChart"] > div {{ background: transparent !important; border: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; }}
    </style>
    """, unsafe_allow_html=True)

def get_chart_config() -> dict:
    t = get_theme()
    is_dark = st.session_state.get("theme", "dark") == "dark"
    return {
        "template": "plotly_dark" if is_dark else "plotly_white",
        "grid_color": "rgba(255,255,255,0.1)" if is_dark else "rgba(0,0,0,0.1)",
        "tick_color": t["text_secondary"],
        "text_color": t["text"],
        "common_layout": {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "font": dict(family="Inter, sans-serif", color=t["text"])
        }
    }