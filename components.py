import streamlit as st
from styles import apply_custom_css, get_theme

def setup_page(title: str, icon: str, page_id: str):
    st.set_page_config(page_title=f"MedInsight | {title}", page_icon=icon, layout="wide", initial_sidebar_state="expanded")
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    st.session_state.current_page = page_id
    apply_custom_css()
    return get_theme()

def render_sidebar(module_name: str, icon: str):
    t = get_theme()
    with st.sidebar:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:0 0 1rem;border-bottom:1px solid {t['border']};margin-bottom:1rem;">
            <div style="width:32px;height:32px;background:linear-gradient(135deg,{t['accent']},{t['info']});
                        border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;">{icon}</div>
            <span style="font-size:1.15rem;font-weight:700;color:{t['text']};">MedInsight Control</span>
        </div>
        """, unsafe_allow_html=True)

        is_dark = st.session_state.theme == "dark"
        if st.toggle("🌙 Dark mode" if is_dark else "☀️ Light mode", value=is_dark, key=f"theme_{module_name}") != is_dark:
            st.session_state.theme = "light" if is_dark else "dark"
            st.rerun()

        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;background:{t['accent_dim']};
                    border:1px solid {t['accent']};border-radius:10px;margin-top:1rem;">
            <span style="height:8px;width:8px;background:{t['accent']};border-radius:50%;box-shadow:0 0 8px {t['accent']};"></span>
            <span style="color:{t['accent']};font-weight:600;font-size:0.875rem;letter-spacing:0.06em;">SYSTEM LIVE</span>
        </div>
        """, unsafe_allow_html=True)
    return t

def render_kpi(col, label: str, value: str, sub: str, color: str, icon: str = ""):
    t = get_theme()
    col.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-label">{icon} {label}</div>
        <div class="kpi-value" style="color:{color}!important;">{value}</div>
        <div style="font-size:0.875rem;color:{t['text_secondary']};margin-top:4px;">{sub}</div>
    </div>
    """, unsafe_allow_html=True)
    
def render_header(title: str, subtitle: str, icon: str, right_badge: str = "", right_color: str = ""):
    t = get_theme()
    badge_html = f'<span style="margin-left:auto;font-size:0.82rem;font-weight:600;color:{right_color};border:1px solid {right_color};padding:3px 14px;border-radius:99px;">{right_badge}</span>' if right_badge else ""
    st.markdown(f"""
    <div style="margin-bottom:1.5rem; display:flex; flex-direction:column;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:4px;">
            <span style="font-size:1.5rem;">{icon}</span>
            <h1 style="margin:0;font-size:1.85rem;font-weight:700;color:{t['text']};">{title}</h1>
            {badge_html}
        </div>
        <p style="margin:0;font-size:0.95rem;color:{t['text_secondary']};">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)