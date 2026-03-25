import streamlit as st
import time
import streamlit.components.v1 as components
from components import setup_page, render_sidebar

# ═══════════════════════════════════════════════════════════════
# 1. PAGE CONFIG & ARCHITECTURE
# ═══════════════════════════════════════════════════════════════
t = setup_page("Command Centre", "⬡", "welcome")
render_sidebar("welcome", "⬡")
current_theme = st.session_state.theme

st.markdown("""
<style>
/* 🚨 THE FIX: Bring transparent header to the absolute front 🚨 */
header[data-testid="stHeader"] {
    background-color: transparent !important;
    box-shadow: none !important;
    z-index: 99999 !important; /* Force above the hero wrapper */
}

/* Style the sidebar toggle button so it's actually visible against the video */
[data-testid="collapsedControl"] {
    background-color: rgba(15, 19, 24, 0.6) !important;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px !important;
    color: #ffffff !important;
    margin: 10px;
    transition: all 0.2s ease;
}

[data-testid="collapsedControl"]:hover {
    background-color: rgba(15, 19, 24, 0.9) !important;
    border-color: #00ff88 !important;
    color: #00ff88 !important;
}

/* Hide the top-right toolbar, footer, and decoration line */
[data-testid="stToolbar"], footer, [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
    display: none !important;
}

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"], [data-testid="stMain"], .main, .stApp {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# 2. YOUR CUSTOM THEME TOKENS
# ═══════════════════════════════════════════════════════════════
if current_theme == "dark":
    video_filter   = "brightness(50%) contrast(115%) saturate(110%)"
    hero_gradient  = "linear-gradient(110deg, #00d4ff 0%, #00ff88 60%, #58a6ff 100%)"
    sub_color      = "#8b949e"
    tag_bg         = "rgba(0,0,0,0.5)"
    tag_border     = "rgba(0,255,136,0.3)"
    tag_color      = "#00ff88"
    stat_label_c   = "#8b949e"
    stat_value_c   = "#00d4ff"
    pulse_color    = "rgba(0,212,255,0.15)"
else:
    video_filter   = "brightness(80%) contrast(95%) saturate(80%) blur(2px)"
    hero_gradient  = "linear-gradient(110deg, #0052cc 0%, #0070f3 55%, #2563eb 100%)"
    sub_color      = "#475569"
    tag_bg         = "rgba(255,255,255,0.65)"
    tag_border     = "rgba(0,112,243,0.25)"
    tag_color      = "#0070f3"
    stat_label_c   = "#64748b"
    stat_value_c   = "#0052cc"
    pulse_color    = "rgba(0,82,204,0.12)"

# ═══════════════════════════════════════════════════════════════
# 3. PRODUCTION HACK: PERSISTENT BACKGROUND VIDEO
# ═══════════════════════════════════════════════════════════════
VIDEO_ID = "zmGV4TFFK9g"

components.html(f"""
<script>
const parentDoc = window.parent.document;
if (!parentDoc.getElementById('persistent-yt-bg')) {{
    const div = parentDoc.createElement('div');
    div.id = 'persistent-yt-bg';
    div.style.position = 'fixed';
    div.style.top = '0';
    div.style.left = '0';
    div.style.width = '100vw';
    div.style.height = '100vh';
    div.style.zIndex = '-999';
    div.style.pointerEvents = 'none';
    div.style.overflow = 'hidden';
    
    div.innerHTML = `
        <iframe src="https://www.youtube.com/embed/{VIDEO_ID}?autoplay=1&mute=1&loop=1&playlist={VIDEO_ID}&controls=0&showinfo=0&modestbranding=1&rel=0&playsinline=1" 
        style="width: 100vw; height: 56.25vw; min-height: 100vh; min-width: 177.78vh; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border: none; filter: {video_filter}; transition: filter 0.5s ease;" 
        allow="autoplay; encrypted-media" allowfullscreen></iframe>
    `;
    parentDoc.body.appendChild(div);
}} else {{
    const iframe = parentDoc.getElementById('persistent-yt-bg').querySelector('iframe');
    if (iframe) iframe.style.filter = "{video_filter}";
}}
</script>
""", height=0, width=0)

# ═══════════════════════════════════════════════════════════════
# 4. YOUR ORIGINAL STUNNING HERO UI
# ═══════════════════════════════════════════════════════════════
ts = time.strftime("%Y-%m-%d  %H:%M:%S UTC", time.gmtime())

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;500;600&display=swap');

.welcome-viewport {{
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    min-height: 100vh; width: 100%;
    position: relative; z-index: 10;
    text-align: center; padding: 2rem;
    pointer-events: none;
}}
@keyframes logo-spin {{
    0%   {{ transform: rotate(0deg);   opacity: 0.6; }}
    50%  {{ transform: rotate(180deg); opacity: 1; }}
    100% {{ transform: rotate(360deg); opacity: 0.6; }}
}}
.hero-logomark {{
    font-size: 3.5rem; line-height: 1; margin-bottom: 1.5rem;
    display: inline-block; animation: logo-spin 12s linear infinite;
    filter: drop-shadow(0 0 20px {tag_color});
}}
@keyframes hero-reveal {{
    0%   {{ opacity: 0; transform: translateY(30px) scale(0.97); letter-spacing: 40px; }}
    100% {{ opacity: 1; transform: translateY(0) scale(1); letter-spacing: 6px; }}
}}
.hero-title {{
    font-family: 'Orbitron', monospace;
    font-size: clamp(48px, 10vw, 130px); font-weight: 900;
    background: {hero_gradient};
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    letter-spacing: 6px; margin: 0; padding: 0; line-height: 1.05; text-transform: uppercase;
    animation: hero-reveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.2s both;
}}
@keyframes sub-reveal {{
    0%   {{ opacity: 0; transform: translateY(12px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}
.hero-subtitle {{
    font-family: 'Inter', sans-serif; color: {sub_color} !important;
    font-size: clamp(0.75rem, 1.5vw, 0.95rem); letter-spacing: 10px;
    text-transform: uppercase; margin-top: 1.25rem; font-weight: 500;
    animation: sub-reveal 0.9s ease 0.9s both;
}}
@keyframes tag-reveal {{
    0%   {{ opacity: 0; transform: translateY(8px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}
.entry-tag {{
    display: inline-flex; align-items: center; gap: 10px;
    margin-top: 2.5rem; padding: 10px 22px;
    background: {tag_bg}; border: 1px solid {tag_border}; border-radius: 99px;
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    animation: tag-reveal 0.8s ease 1.4s both; pointer-events: auto;
}}
.entry-dot {{
    width: 7px; height: 7px; background: {tag_color}; border-radius: 50%;
    box-shadow: 0 0 8px {tag_color}; animation: blink 1.6s ease-in-out infinite;
}}
.entry-text {{
    font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 600;
    letter-spacing: 0.14em; text-transform: uppercase; color: {tag_color} !important;
}}
@keyframes pills-reveal {{
    0%   {{ opacity: 0; transform: translateY(14px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}
.stat-row {{
    display: flex; gap: 1rem; margin-top: 3rem;
    flex-wrap: wrap; justify-content: center;
    animation: pills-reveal 0.8s ease 1.8s both; pointer-events: auto;
}}
.stat-pill {{
    display: flex; flex-direction: column; align-items: center;
    padding: 14px 28px; background: {tag_bg}; border: 1px solid {tag_border};
    border-radius: 14px; backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    min-width: 120px; cursor: default; transition: all 0.2s ease;
}}
.stat-pill:hover {{
    border-color: {tag_color}; transform: translateY(-2px);
    box-shadow: 0 8px 24px {pulse_color};
}}
.stat-value {{
    font-family: 'Orbitron', monospace; font-size: 1.4rem; font-weight: 700;
    color: {stat_value_c} !important; line-height: 1;
}}
.stat-label {{
    font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    color: {stat_label_c} !important; margin-top: 6px;
}}
.corner-stamp {{
    position: fixed; bottom: 1.5rem; right: 2rem;
    font-family: 'Orbitron', monospace; font-size: 0.65rem;
    color: {stat_label_c} !important; letter-spacing: 0.1em;
    opacity: 0.7; z-index: 50; pointer-events: none;
}}
</style>

<div class="welcome-viewport">
    <div class="hero-logomark">⬡</div>
    <h1 class="hero-title">MedInsight</h1>
    <p class="hero-subtitle">Unified Command &nbsp;·&nbsp; Secure Operations Centre</p>
    <div class="entry-tag">
        <span class="entry-dot"></span>
        <span class="entry-text">Authorized Access Only &nbsp;— &nbsp;Session Authenticated</span>
    </div>
    <div class="stat-row">
        <div class="stat-pill">
            <span class="stat-value">99.9%</span>
            <span class="stat-label">Uptime</span>
        </div>
        <div class="stat-pill">
            <span class="stat-value">0</span>
            <span class="stat-label">Critical Alerts</span>
        </div>
        <div class="stat-pill">
            <span class="stat-value">TLS</span>
            <span class="stat-label">Encrypted</span>
        </div>
        <div class="stat-pill">
            <span class="stat-value">LIVE</span>
            <span class="stat-label">Data Feed</span>
        </div>
    </div>
</div>
<div class="corner-stamp">{ts}</div>
""", unsafe_allow_html=True)