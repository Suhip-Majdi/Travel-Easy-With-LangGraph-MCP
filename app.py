import os
import streamlit as st
from datetime import datetime
from langchain_core.messages import HumanMessage
from main import app

st.set_page_config(
    page_title="AI Travel Booking System",
    page_icon="🎫",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
    --paper:      #FBF7EE;
    --paper-dim:  #F1EADA;
    --ink:        #1A2B3C;
    --ink-soft:   #4A5A6B;
    --terracotta: #C75D3A;
    --terracotta-dim: #C75D3A33;
    --sage:       #5B8A72;
    --gold:       #D4A24C;
    --stub-edge:  #D8CFB8;
}

html, body, .stApp {
    font-family: 'Space Grotesk', sans-serif;
    background-color: var(--paper);
    color: var(--ink);
}

/* ── Perforation divider, the signature motif ── */
.perf {
    border: none;
    height: 1px;
    margin: 2rem 0;
    background-image: repeating-linear-gradient(to right, var(--stub-edge) 0 8px, transparent 8px 16px);
}

/* ── Hero: the "ticket" ── */
.ticket-wrapper {
    position: relative;
    background: var(--ink);
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 1.4rem;
    display: flex;
    min-height: 240px;
    box-shadow: 0 14px 34px rgba(26,43,60,0.22);
}
.ticket-main {
    position: relative;
    flex: 1;
    padding: 2.2rem 2.4rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
}
.ticket-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    object-fit: cover;
    opacity: 0.28;
    filter: saturate(0.7) contrast(1.05);
}
.ticket-eyebrow {
    position: relative;
    z-index: 2;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.7rem;
}
.ticket-title {
    position: relative;
    z-index: 2;
    font-family: 'Fraunces', serif;
    font-size: 2.5rem;
    font-weight: 600;
    color: #FBF7EE;
    margin: 0 0 0.5rem;
    line-height: 1.1;
}
.ticket-sub {
    position: relative;
    z-index: 2;
    color: #C9D4DE;
    font-size: 0.98rem;
    max-width: 480px;
    line-height: 1.5;
}
.ticket-stub {
    position: relative;
    width: 190px;
    background: #16222F;
    border-left: 2px dashed #3A4D5E;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 1.5rem 1rem;
}
.ticket-stub::before, .ticket-stub::after {
    content: "";
    position: absolute;
    width: 22px; height: 22px;
    background: var(--paper);
    border-radius: 50%;
    left: -11px;
}
.ticket-stub::before { top: -11px; }
.ticket-stub::after { bottom: -11px; }
.stub-code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--gold);
    letter-spacing: 0.05em;
}
.stub-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7A8DA0;
    text-align: center;
}
.stub-divider { width: 60%; height: 1px; background: #3A4D5E; margin: 0.3rem 0; }

/* ── Destination stamp strip ── */
.stamp-card {
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    height: 100px;
    cursor: pointer;
    border: 2px solid var(--paper);
    outline: 1px solid var(--stub-edge);
    transition: transform 0.15s ease, outline-color 0.15s ease;
}
.stamp-card:hover { transform: rotate(-1deg) scale(1.02); outline-color: var(--terracotta); }
.stamp-img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.6) saturate(0.9); }
.stamp-label {
    position: absolute; bottom: 6px; left: 0; right: 0; text-align: center;
    color: #fff; font-size: 0.78rem; font-weight: 600;
    font-family: 'Space Grotesk', sans-serif;
}
.stamp-corner {
    position: absolute; top: 6px; right: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem; color: var(--gold);
    border: 1px solid var(--gold);
    border-radius: 4px; padding: 1px 5px;
    background: rgba(0,0,0,0.35);
    letter-spacing: 0.05em;
}

/* ── Input card: looks like a ticket request form ── */
.input-card {
    background: #fff;
    border: 1px solid var(--stub-edge);
    border-radius: 16px;
    padding: 1.5rem 1.7rem 0.4rem;
    margin: 1.6rem 0 0.4rem;
    box-shadow: 0 2px 10px rgba(26,43,60,0.05);
}
.input-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    color: var(--terracotta);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.7rem;
}

/* Quick-pick chips reuse Streamlit buttons inside input card */
div[data-testid="column"] .stButton > button {
    background: var(--paper-dim) !important;
    color: var(--ink) !important;
    border: 1px solid var(--stub-edge) !important;
    border-radius: 999px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.4rem 1rem !important;
    box-shadow: none !important;
    width: auto !important;
    transition: all 0.15s ease !important;
}
div[data-testid="column"] .stButton > button:hover {
    background: var(--terracotta) !important;
    color: #fff !important;
    border-color: var(--terracotta) !important;
    transform: none !important;
}

/* ── Generate button: the main "Issue ticket" CTA ── */
div[data-testid="stButton"]:has(button:contains("Generate")) { }
.generate-btn-wrap button {
    background: var(--terracotta) !important;
    color: #FBF7EE !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.9rem 2.4rem !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    width: 100% !important;
    box-shadow: 0 6px 18px rgba(199,93,58,0.32) !important;
    transition: all 0.2s ease !important;
}
.generate-btn-wrap button:hover {
    background: #B14E2C !important;
    box-shadow: 0 8px 22px rgba(199,93,58,0.42) !important;
    transform: translateY(-2px) !important;
}
.generate-btn-wrap button:active { transform: translateY(0) !important; }

/* ── Agent status cards: ticket stages ── */
[data-testid="stStatusWidget"] {
    background: #fff !important;
    border: 1px solid var(--stub-edge) !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(26,43,60,0.04) !important;
}
[data-testid="stStatusWidget"] > div:first-child {
    background: var(--paper-dim) !important;
    border-radius: 12px 12px 0 0 !important;
}
[data-testid="stStatusWidget"] details,
[data-testid="stStatusWidget"] details > div,
[data-testid="stStatusWidget"] [data-testid="stVerticalBlock"] {
    background: #fff !important;
    color: var(--ink) !important;
    padding: 0.3rem 0.6rem !important;
}
[data-testid="stStatusWidget"] * { color: var(--ink) !important; font-family: 'Space Grotesk', sans-serif !important; }
[data-testid="stStatusWidget"] a { color: var(--terracotta) !important; }
[data-testid="stStatusWidget"] hr { border-color: var(--stub-edge) !important; }
[data-testid="stStatusWidget"] p[data-testid="stMarkdownContainer"]:first-child,
[data-testid="stStatusWidget"] label { font-family: 'JetBrains Mono', monospace !important; font-weight: 600 !important; }

/* ── Section headers ── */
.sec-head {
    display: flex;
    align-items: baseline;
    gap: 0.7rem;
    margin: 2rem 0 0.9rem;
}
.sec-head .sec-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--terracotta);
    font-weight: 700;
    border: 1.5px solid var(--terracotta);
    border-radius: 5px;
    padding: 0.1rem 0.45rem;
}
.sec-head span.sec-title {
    font-family: 'Fraunces', serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--ink);
}

/* ── Metric strip: like a baggage-tag readout ── */
.metric-row { display: flex; gap: 0; margin: 1.6rem 0; border-radius: 12px; overflow: hidden; border: 1px solid var(--stub-edge); }
.metric-box {
    flex: 1;
    background: #fff;
    padding: 1.1rem 1rem;
    text-align: center;
    border-right: 1px dashed var(--stub-edge);
}
.metric-box:last-child { border-right: none; }
.metric-val { font-family: 'JetBrains Mono', monospace; font-size: 1.7rem; font-weight: 700; color: var(--terracotta); }
.metric-lbl { font-size: 0.72rem; color: var(--ink-soft); margin-top: 0.25rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }

/* ── Final plan: folded itinerary card ── */
.final-card {
    background: #fff;
    border: 1px solid var(--stub-edge);
    border-left: 5px solid var(--sage);
    border-radius: 4px 14px 14px 4px;
    padding: 2rem 2.2rem;
    line-height: 1.8;
    color: var(--ink);
    font-size: 0.97rem;
    position: relative;
    box-shadow: 0 4px 16px rgba(26,43,60,0.06);
}
.final-card::before {
    content: "CONFIRMED";
    position: absolute;
    top: 1.4rem; right: 1.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--sage);
    border: 1.5px solid var(--sage);
    border-radius: 5px;
    padding: 0.15rem 0.5rem;
    transform: rotate(3deg);
}

/* ── Save bar ── */
.save-bar {
    background: var(--paper-dim);
    border: 1px dashed var(--stub-edge);
    border-radius: 10px;
    padding: 0.8rem 1.1rem;
    color: var(--ink-soft);
    font-size: 0.85rem;
    margin-top: 0.6rem;
    font-family: 'JetBrains Mono', monospace;
}
.save-bar code { color: var(--terracotta); background: transparent; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--ink) !important;
    border-right: none !important;
}
.sidebar-title {
    font-family: 'JetBrains Mono', monospace;
    color: var(--gold);
    font-size: 0.74rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin: 1.2rem 0 0.6rem;
}
.sidebar-chip {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.4rem;
    font-size: 0.83rem;
    color: #C9D4DE;
    font-family: 'Space Grotesk', sans-serif;
}
section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.12) !important; }
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown { color: #C9D4DE !important; }

/* Sidebar text input */
section[data-testid="stSidebar"] input[type="text"] {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 8px !important;
    color: #FBF7EE !important;
    font-family: 'JetBrains Mono', monospace !important;
}
section[data-testid="stSidebar"] input[type="text"]:focus {
    border-color: var(--terracotta) !important;
    box-shadow: 0 0 0 2px var(--terracotta-dim) !important;
}
section[data-testid="stSidebar"] input[type="text"]::placeholder { color: #6A7E90 !important; }

/* Hide branding */
#MainMenu, footer, header { visibility: hidden; }

/* Textarea */
.stTextArea textarea {
    background: #fff !important;
    border: 1px solid var(--stub-edge) !important;
    border-radius: 10px !important;
    color: var(--ink) !important;
    font-size: 0.97rem !important;
    font-family: 'Space Grotesk', sans-serif !important;
    resize: none !important;
}
.stTextArea textarea:focus {
    border-color: var(--terracotta) !important;
    box-shadow: 0 0 0 2px var(--terracotta-dim) !important;
}
.stTextArea textarea::placeholder { color: #9AA8B5 !important; }

/* Labels */
.stTextInput label, .stTextArea label,
.stSelectbox label, .stNumberInput label {
    color: var(--terracotta) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
}

/* General markdown / paragraph text */
.stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th { color: var(--ink) !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: var(--ink) !important; font-family: 'Fraunces', serif !important; }
.stMarkdown code {
    background: var(--paper-dim) !important;
    color: var(--terracotta) !important;
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Streamlit warning / info / success on light paper bg */
.stAlert { background: #fff !important; border: 1px solid var(--stub-edge) !important; border-radius: 10px !important; }
.stAlert p, .stAlert div { color: var(--ink) !important; }

/* Download button */
div[data-testid="stDownloadButton"] > button {
    background: var(--sage) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
}
div[data-testid="stDownloadButton"] > button:hover {
    background: #4A7560 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div class='sidebar-title'>🎫 Boarding Pass</div>", unsafe_allow_html=True)
    st.markdown("---")

    thread_id = st.text_input("Passenger ID", value="Suhip_user",
                              help="Your session ID — keeps travel history across queries")

    st.markdown("<div class='sidebar-title'>Powered by</div>", unsafe_allow_html=True)
    for tech in ["🔗 LangGraph", "🧠 Groq · LLaMA 3.3 70B", "🐘 PostgreSQL", "🔍 Tavily Search", "✈️ AviationStack"]:
        st.markdown(f"<div class='sidebar-chip'>{tech}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-title'>Agent Pipeline</div>", unsafe_allow_html=True)
    for step in ["① Flight Agent", "② Hotel Agent", "③ Itinerary Agent", "④ Final Agent"]:
        st.markdown(f"<div class='sidebar-chip'>{step}</div>", unsafe_allow_html=True)

# ── Hero: the ticket ──────────────────────────────────────────────────────────
st.markdown("""
<div class="ticket-wrapper">
    <div class="ticket-main">
        <img class="ticket-bg"
             src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80"
             alt="airplane above clouds"/>
        <div class="ticket-eyebrow">✦ Multi-Agent Issue · Class: AI</div>
        <div class="ticket-title">AI Travel Booking System</div>
        <div class="ticket-sub">Four specialized agents work the counter for you — flights, hotels, itinerary, and a final plan, stapled together like a real ticket.</div>
    </div>
    <div class="ticket-stub">
        <div class="stub-code">PLAN</div>
        <div class="stub-label">Boarding Group</div>
        <div class="stub-divider"></div>
        <div class="stub-code" style="font-size:1.1rem;">4 / 4</div>
        <div class="stub-label">Agents Onboard</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Destination stamp strip ───────────────────────────────────────────────────
DESTINATIONS = [
    ("Tokyo",   "NRT", "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&q=70"),
    ("Paris",   "CDG", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&q=70"),
    ("Bangkok", "BKK", "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=300&q=70"),
    ("Rome",    "FCO", "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=300&q=70"),
    ("Dubai",   "DXB", "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&q=70"),
]

cols = st.columns(5)
for col, (name, code, img_url) in zip(cols, DESTINATIONS):
    with col:
        st.markdown(f"""
        <div class="stamp-card">
            <img src="{img_url}" class="stamp-img" />
            <div class="stamp-corner">{code}</div>
            <div class="stamp-label">{name}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div class='perf'></div>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
st.markdown("<div class='input-eyebrow'>🗺️ Describe your trip</div>", unsafe_allow_html=True)

QUICK = ["7-day Japan under 2000 JD", "Paris trip for 5 days", "Dubai weekend trip", "Bali backpacking 10 days"]
qcols = st.columns(len(QUICK))
quick_fill = ""
for qc, label in zip(qcols, QUICK):
    with qc:
        if st.button(label, key=f"q_{label}"):
            quick_fill = label

user_query = st.text_area(
    "",
    value=quick_fill,
    placeholder="e.g. Plan a complete 7-day Paris trip including flights, hotels and sightseeing under 1000 JD",
    height=100,
    label_visibility="collapsed",
)

st.markdown('<div class="generate-btn-wrap">', unsafe_allow_html=True)
generate = st.button("🎫  Issue My Travel Plan", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Agent pipeline ────────────────────────────────────────────────────────────
AGENT_META = {
    "flight_agent":    ("✈️", "Flight Agent",    "01"),
    "hotel_agent":     ("🏨", "Hotel Agent",     "02"),
    "itinerary_agent": ("🗓️", "Itinerary Agent", "03"),
    "final_agent":     ("🧠", "Final Agent",     "04"),
}

if generate:
    if not user_query.strip():
        st.warning("Please describe your trip first.")
    else:
        config = {"configurable": {"thread_id": thread_id}}
        collected = {"flight_results": "", "hotel_results": "",
                     "itinerary": "", "final_response": "", "llm_calls": 0}

        st.markdown("<div class='perf'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='sec-head'><span class='sec-num'>LIVE</span><span class='sec-title'>Agent Pipeline</span></div>",
            unsafe_allow_html=True)

        for chunk in app.stream(
            {
                "messages": [HumanMessage(content=user_query)],
                "user_query": user_query,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,
            },
            config=config,
            stream_mode="updates",
        ):
            for node_name, state_update in chunk.items():
                icon, label, num = AGENT_META.get(node_name, ("🔧", node_name, "•"))

                with st.status(f"{num} · {icon}  {label}", state="complete", expanded=True):
                    if node_name == "flight_agent":
                        text = state_update.get("flight_results", "")
                        collected["flight_results"] = text
                        st.markdown(text or "_No flight data returned._")

                    elif node_name == "hotel_agent":
                        text = state_update.get("hotel_results", "")
                        collected["hotel_results"] = text
                        st.markdown(text or "_No hotel data returned._")

                    elif node_name == "itinerary_agent":
                        text = state_update.get("itinerary", "")
                        collected["itinerary"] = text
                        st.markdown(text or "_No itinerary generated._")

                    elif node_name == "final_agent":
                        msgs = state_update.get("messages", [])
                        text = msgs[-1].content if msgs else ""
                        collected["final_response"] = text
                        st.markdown(text or "_No final response._")

                    collected["llm_calls"] = state_update.get("llm_calls", collected["llm_calls"])

        # Metrics
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-box"><div class="metric-val">4</div><div class="metric-lbl">Agents Run</div></div>
            <div class="metric-box"><div class="metric-val">{collected['llm_calls']}</div><div class="metric-lbl">LLM Calls</div></div>
            <div class="metric-box"><div class="metric-val">✓</div><div class="metric-lbl">Status</div></div>
        </div>
        """, unsafe_allow_html=True)

        # Final plan card
        if collected["final_response"]:
            st.markdown(
                "<div class='sec-head'><span class='sec-num'>04</span><span class='sec-title'>Your Travel Plan</span></div>",
                unsafe_allow_html=True)
            st.markdown(f"<div class='final-card'>{collected['final_response']}</div>",
                        unsafe_allow_html=True)

        # Save
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.md"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        file_content = f"""# Travel Plan
**Query:** {user_query}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User ID:** {thread_id}

---

## ✈️ Flight Information
{collected['flight_results'] or 'N/A'}

---

## 🏨 Hotel Information
{collected['hotel_results'] or 'N/A'}

---

## 🗓️ Itinerary
{collected['itinerary'] or 'N/A'}

---

## 🧠 Final Travel Plan
{collected['final_response'] or 'N/A'}

---
*LLM Calls: {collected['llm_calls']}*
"""
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(file_content)

        st.markdown("<div class='perf'></div>", unsafe_allow_html=True)
        dl_col, info_col = st.columns([1, 3])
        with dl_col:
            st.download_button("⬇️ Download Plan", data=file_content,
                               file_name=filename, mime="text/markdown",
                               use_container_width=True)
        with info_col:
            st.markdown(f"<div class='save-bar'>📁 AUTO-SAVED → <code>travel_plans/{filename}</code></div>",
                        unsafe_allow_html=True)