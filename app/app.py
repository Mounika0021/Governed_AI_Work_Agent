import streamlit as st

st.set_page_config(
    page_title="Governed AI Work Agent",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# DATA
# ============================================================

PRIMARY_PRODUCT = "Protein Bar"

MERCHANT = {
    "name": "FitFuel Store",
    "category": "Fitness & Nutrition",
    "vertical": "Sports Wellness",
    "subcategories": ["Sports Wellness", "Active Lifestyle", "Workout Essentials"],
    "primary_product": "Protein Bar",
    "orders": 150,
    "repeat_signal": "Strong",
    "cross_sell_signal": "High",
    "customer_segments": [
        "Fitness-focused customers",
        "Nutrition-conscious buyers",
        "Workout accessory shoppers",
    ],
}

PRODUCTS = [
    {
        "name": "Shaker Bottle",
        "category": "Fitness Accessory",
        "role": "Workout Essential",
        "score": 92,
        "customer_fit": 94,
        "category_fit": 91,
        "purchase_relevance": 90,
        "impact": "High",
        "confidence": "Very high",
        "reason": "Strong complementary fit for customers already purchasing sports nutrition products.",
        "evidence": [
            "Complementary fitness category",
            "Strong customer relevance",
            "Existing demand signal",
        ],
    },
    {
        "name": "Protein Cookies",
        "category": "Nutrition",
        "role": "Nutrition Add-on",
        "score": 87,
        "customer_fit": 90,
        "category_fit": 88,
        "purchase_relevance": 84,
        "impact": "Medium–High",
        "confidence": "High",
        "reason": "Natural nutrition cross-sell for the same fitness-focused customer segment.",
        "evidence": [
            "Same customer segment",
            "Natural nutrition complement",
            "Repeat-purchase potential",
        ],
    },
    {
        "name": "Gym Towel",
        "category": "Fitness Accessory",
        "role": "Workout Essential",
        "score": 81,
        "customer_fit": 86,
        "category_fit": 82,
        "purchase_relevance": 79,
        "impact": "Medium",
        "confidence": "High",
        "reason": "Relevant accessory aligned with the merchant fitness customer base.",
        "evidence": [
            "Strong fitness relevance",
            "Complementary accessory",
            "Low-friction purchase category",
        ],
    },
]

STAGES = [
    ("Welcome", "Workspace"),
    ("Merchant", "Business profile"),
    ("Context", "Business signals"),
    ("Analysis", "AI reasoning"),
    ("Opportunities", "Growth discovery"),
    ("Review", "Evidence"),
    ("Governance", "Policy"),
    ("Approval", "Decision"),
    ("Execution", "Controlled action"),
    ("Verification", "Assurance"),
    ("Outcome", "Result"),
    ("Audit", "Traceability"),
    ("Summary", "Executive view"),
]

def merchant_value(key, default="Not available"):
    """Safe UI accessor so a missing optional merchant field never crashes the app."""
    return MERCHANT.get(key, default)

# ============================================================
# SESSION STATE
# ============================================================

if "stage" not in st.session_state:
    st.session_state.stage = 0

if "selected_product" not in st.session_state:
    st.session_state.selected_product = PRODUCTS[0]


def next_stage():
    st.session_state.stage = min(st.session_state.stage + 1, len(STAGES) - 1)
    st.rerun()


def reset_workflow():
    st.session_state.stage = 0
    st.session_state.selected_product = PRODUCTS[0]
    st.rerun()


def select_product(product):
    st.session_state.selected_product = product
    st.session_state.stage = 5
    st.rerun()


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
  --bg:#EEF1F5;
  --surface:#FFFFFF;
  --ink:#172033;
  --body:#46546A;
  --muted:#718096;
  --line:#D9E0E8;
  --primary:#4E5BC6;
  --primary2:#6D67D5;
  --primary-soft:#ECEEF8;
  --success:#17663F;
  --success-bg:#EAF6EF;
  --warning:#68583E;
  --warning-bg:#F4F0E8;
  --info:#42536B;
  --info-bg:#EEF3F8;
}

.stApp {
  background:var(--bg) !important;
  color:var(--ink) !important;
  font-family:"Inter",sans-serif !important;
}

.block-container {
  max-width:1380px;
  padding-top:18px !important;
  padding-bottom:52px !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
  display:none !important;
}

#MainMenu, footer {
  visibility:hidden;
}

h1,h2,h3,h4 {
  font-family:"Plus Jakarta Sans",sans-serif !important;
  color:var(--ink) !important;
  letter-spacing:-.04em !important;
}

[data-testid="stMarkdownContainer"] p {
  color:var(--body) !important;
  line-height:1.62 !important;
}

[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
  color:var(--muted) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
  background:#172033 !important;
  border-right:0 !important;
}

section[data-testid="stSidebar"] .stButton > button {
  background:transparent !important;
  border:0 !important;
  color:#ABB7C9 !important;
  opacity:1 !important;
  box-shadow:none !important;
  min-height:34px !important;
  text-align:left !important;
  border-radius:9px !important;
}

section[data-testid="stSidebar"] .stButton > button:disabled {
  opacity:1 !important;
  color:#ABB7C9 !important;
}

section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
  background:rgba(113,103,213,.19) !important;
  border:1px solid rgba(167,155,255,.18) !important;
  color:#F2F0FF !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
  color:#8F9BB0 !important;
}

.side-brand {
  display:flex;
  align-items:center;
  gap:10px;
  padding:5px 2px 22px;
}

.side-mark {
  width:39px;
  height:39px;
  border-radius:12px;
  background:linear-gradient(135deg,#6D61F4,#9A83FF);
  display:flex;
  align-items:center;
  justify-content:center;
  color:#fff;
  font-family:"Plus Jakarta Sans",sans-serif;
  font-weight:800;
  box-shadow:0 9px 23px rgba(109,97,244,.27);
}

.side-title {
  color:#fff !important;
  font-family:"Plus Jakarta Sans",sans-serif;
  font-size:14px;
  font-weight:800;
}

.side-sub {
  color:#94A0B4 !important;
  font-size:9px;
  margin-top:2px;
}

/* topbar */
.topbar {
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:2px 0 12px;
  border-bottom:1px solid var(--line);
  margin-bottom:12px;
}

.brand-lock {
  display:flex;
  align-items:center;
  gap:10px;
}

.brand-symbol {
  width:37px;
  height:37px;
  border-radius:11px;
  background:linear-gradient(135deg,#4E5BC6,#7568DB);
  display:flex;
  align-items:center;
  justify-content:center;
  color:#fff;
  font-weight:800;
}

.brand-title {
  color:var(--ink);
  font-family:"Plus Jakarta Sans",sans-serif;
  font-size:15px;
  font-weight:800;
}

.brand-sub {
  color:var(--muted);
  font-size:10px;
  margin-top:1px;
}

.environment {
  background:#F1F9F4;
  border:1px solid #CFE4D7;
  color:#2A7650;
  border-radius:999px;
  padding:7px 11px;
  font-size:9px;
  font-weight:800;
}

/* native containers */
[data-testid="stVerticalBlockBorderWrapper"] {
  background:#fff !important;
  border:1px solid var(--line) !important;
  border-radius:15px !important;
  box-shadow:0 5px 18px rgba(17,24,39,.03) !important;
}

/* metrics */
[data-testid="stMetric"] {
  background:#fff !important;
  border:1px solid var(--line) !important;
  border-radius:13px !important;
  padding:13px 15px !important;
}

[data-testid="stMetricLabel"] {
  color:#617086 !important;
  font-size:10px !important;
}

[data-testid="stMetricValue"] {
  color:var(--ink) !important;
  font-family:"Plus Jakarta Sans",sans-serif !important;
  font-weight:800 !important;
}

/* progress */
[data-testid="stProgressBar"] > div {
  height:5px !important;
  background:#E4E8EE !important;
  border-radius:99px !important;
}

[data-testid="stProgressBar"] > div > div > div > div {
  background:linear-gradient(90deg,#4E5BC6,#7A6DDF) !important;
  border-radius:99px !important;
}

/* buttons */
.stButton > button {
  min-height:41px !important;
  border-radius:10px !important;
  border:1px solid #C8D0DA !important;
  background:#fff !important;
  color:#344054 !important;
  font-family:"Inter",sans-serif !important;
  font-size:12px !important;
  font-weight:700 !important;
}

.stButton > button:hover {
  background:#F8FAFC !important;
  border-color:#98A2B3 !important;
  color:#172033 !important;
}

.stButton > button[kind="primary"] {
  border:0 !important;
  background:linear-gradient(135deg,#4E5BC6,#6767D5) !important;
  color:#fff !important;
  box-shadow:0 8px 18px rgba(78,91,198,.18);
}

.stButton > button[kind="primary"] * {
  color:#fff !important;
}

/* alerts */
[data-testid="stAlert"] {
  border-radius:12px !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="positive"] {
  background:#EAF6EF !important;
  border:1px solid #B9E2C8 !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="positive"] p,
[data-testid="stAlert"][data-baseweb="notification"][kind="positive"] div {
  color:#17663F !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
  background:#EEF3F8 !important;
  border:1px solid #D2DCE8 !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="info"] p,
[data-testid="stAlert"][data-baseweb="notification"][kind="info"] div {
  color:#42536B !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
  background:#F4F0E8 !important;
  border:1px solid #D9CFBA !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] p,
[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] div {
  color:#68583E !important;
}

/* hero */
.hero {
  border-radius:21px;
  padding:37px 40px;
  min-height:235px;
  background:
    radial-gradient(circle at 85% 14%,rgba(148,134,255,.32),transparent 23%),
    linear-gradient(122deg,#121C36,#24356F 55%,#5B43A2);
  color:#fff;
  box-shadow:0 18px 45px rgba(35,40,94,.14);
}

.hero-kicker {
  color:#C9D1FF;
  font-size:9px;
  font-weight:800;
  letter-spacing:.16em;
  text-transform:uppercase;
}

.hero-title {
  color:#fff;
  font-family:"Plus Jakarta Sans",sans-serif;
  font-size:41px;
  line-height:1.04;
  font-weight:800;
  letter-spacing:-.055em;
  margin-top:10px;
}

.hero-copy {
  color:#E0E5F7;
  max-width:700px;
  font-size:13px;
  line-height:1.65;
  margin-top:13px;
}

.hero-pills {
  display:flex;
  gap:7px;
  flex-wrap:wrap;
  margin-top:20px;
}

.hero-pill {
  color:#F3F4FF;
  background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.13);
  padding:6px 9px;
  border-radius:999px;
  font-size:9px;
  font-weight:700;
}

/* generic */
.eyebrow {
  color:var(--primary);
  font-size:9px;
  font-weight:800;
  letter-spacing:.15em;
  text-transform:uppercase;
}

.page-title {
  color:var(--ink);
  font-family:"Plus Jakarta Sans",sans-serif;
  font-size:29px;
  font-weight:800;
  letter-spacing:-.045em;
  margin-top:2px;
}

.page-copy {
  color:var(--body);
  font-size:13px;
  line-height:1.6;
  margin:5px 0 19px;
}

.context-chip {
  display:inline-block;
  background:#F1F3F8;
  color:#4B5870;
  padding:6px 9px;
  margin:3px 4px 3px 0;
  border-radius:999px;
  font-size:9px;
  font-weight:700;
}

.score-track {
  height:5px;
  width:100%;
  background:#E8EBF0;
  border-radius:99px;
  margin-top:7px;
}

.score-fill {
  height:5px;
  background:linear-gradient(90deg,#4E5BC6,#7A6DDF);
  border-radius:99px;
}

.score-big {
  color:var(--primary);
  font-family:"Plus Jakarta Sans",sans-serif;
  font-size:28px;
  font-weight:800;
}

.small-label {
  color:#7C8799;
  font-size:9px;
  font-weight:800;
  letter-spacing:.1em;
  text-transform:uppercase;
}

.reason-box {
  background:#F8F9FC;
  border:1px solid #E7EAF0;
  border-radius:12px;
  padding:14px;
  color:#435168;
  font-size:11px;
  line-height:1.6;
}

.timeline-line {
  display:flex;
  align-items:center;
  gap:12px;
  padding:11px 0;
  border-bottom:1px solid #F0F2F5;
}

.timeline-line:last-child {
  border-bottom:0;
}

.timeline-dot {
  width:27px;
  height:27px;
  border-radius:50%;
  background:#ECEEF8;
  color:#4E5BC6;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:8px;
  font-weight:800;
  flex:0 0 27px;
}

.timeline-label {
  color:#344054;
  font-size:11px;
  font-weight:650;
}

.timeline-status {
  margin-left:auto;
  color:#18794E;
  font-size:9px;
  font-weight:800;
}

.app-footer {
  border-top:1px solid var(--line);
  margin-top:35px;
  padding-top:13px;
  display:flex;
  justify-content:space-between;
  color:#718096 !important;
  font-size:9px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div class="side-brand">
            <div class="side-mark">✦</div>
            <div>
                <div class="side-title">Governed AI</div>
                <div class="side-sub">Decision intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("WORKFLOW")

    for i, (name, _) in enumerate(STAGES):
        if i < st.session_state.stage:
            label = f"✓  {name}"
        elif i == st.session_state.stage:
            label = f"●  {name}"
        else:
            label = f"{i+1:02d}  {name}"

        st.button(
            label,
            key=f"sidebar_{i}",
            type="primary" if i == st.session_state.stage else "secondary",
            disabled=True,
            use_container_width=True,
        )

    st.divider()
    st.caption("PLATFORM")
    st.caption("Merchant intelligence")
    st.caption("Growth opportunities")
    st.caption("Governance & assurance")

    st.divider()
    st.markdown(
        """
        <div style="color:#8F9BB0;font-size:9px;font-weight:800;letter-spacing:.12em;">
            AGENT STATUS
        </div>
        <div style="color:#D1D8E4;font-size:11px;font-weight:700;margin-top:7px;">
            ● Online
        </div>
        <div style="color:#8F9BB0;font-size:9px;margin-top:2px;">
            Governed decision operator
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# TOP BAR + PROGRESS
# ============================================================

stage = st.session_state.stage
stage_name, stage_desc = STAGES[stage]
percent = int(((stage + 1) / len(STAGES)) * 100)

st.markdown(
    f"""
    <div class="topbar">
        <div class="brand-lock">
            <div class="brand-symbol">✦</div>
            <div>
                <div class="brand-title">Governed AI Work Agent</div>
                <div class="brand-sub">Merchant decision intelligence workspace</div>
            </div>
        </div>
        <div class="environment">● SIMULATION · EXTERNAL ACTIONS DISABLED</div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    left, right = st.columns([5, 1])
    with left:
        st.caption("WORKFLOW PROGRESS")
        st.markdown(f"**{stage_name} · {stage_desc}**")
    with right:
        st.markdown(f"**{percent}%**")
        st.caption(f"Stage {stage + 1} / {len(STAGES)}")

st.progress((stage + 1) / len(STAGES))

# ============================================================
# 01 WELCOME
# ============================================================

if stage == 0:

    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">Decision intelligence · governed automation</div>
            <div class="hero-title">Turn business signals<br>into governed action.</div>
            <div class="hero-copy">
                Discover growth opportunities, understand agent reasoning,
                validate policy, review the proposed action and verify the
                result through one controlled decision journey.
            </div>
            <div class="hero-pills">
                <span class="hero-pill">AI-assisted decisions</span>
                <span class="hero-pill">Evidence driven</span>
                <span class="hero-pill">Policy controlled</span>
                <span class="hero-pill">Audit ready</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="eyebrow">PLATFORM OVERVIEW</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">One workspace. One governed decision journey.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">The agent connects merchant intelligence, recommendations, governance and assurance in one workflow.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.caption("01 · INTELLIGENCE")
            st.subheader("Discover")
            st.write("Find relevant growth opportunities from business and product signals.")

    with c2:
        with st.container(border=True):
            st.caption("02 · GOVERNANCE")
            st.subheader("Control")
            st.write("Apply policy and approval checks before a proposed action progresses.")

    with c3:
        with st.container(border=True):
            st.caption("03 · ASSURANCE")
            st.subheader("Verify")
            st.write("Validate the decision path and preserve a traceable outcome.")

    st.info("Controlled simulation · No external merchant system will be changed.")

    if st.button("Start merchant analysis  →", type="primary"):
        next_stage()

# ============================================================
# 02 MERCHANT PROFILE
# ============================================================

elif stage == 1:

    st.markdown('<div class="eyebrow">MERCHANT INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Business profile</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Establish the business and customer context used by the agent.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([2.8, 1.2])

    with c1:
        with st.container(border=True):
            st.caption("BUSINESS")
            st.subheader(merchant_value("name"))
            st.write(f"{merchant_value('category')} · {merchant_value('vertical')}")
            for tag in MERCHANT.get("subcategories", []):
                st.markdown(f'<span class="context-chip">{tag}</span>', unsafe_allow_html=True)

    with c2:
        with st.container(border=True):
            st.caption("PRIMARY PRODUCT")
            st.subheader(PRIMARY_PRODUCT)
            st.caption("Core purchase signal")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">CUSTOMER PROFILE</div>', unsafe_allow_html=True)

    with st.container(border=True):
        for item in MERCHANT.get("customer_segments", []):
            st.write(f"✓  {item}")

    a, b, c = st.columns(3)
    with a:
        st.metric("Orders observed", merchant_value("orders"))
    with b:
        st.metric("Repeat signal", merchant_value("repeat_signal"))
    with c:
        st.metric("Cross-sell potential", merchant_value("cross_sell_signal"))

    st.success("Business context is ready for analysis.")

    if st.button("Continue to business signals  →", type="primary"):
        next_stage()

# ============================================================
# 03 CONTEXT
# ============================================================

elif stage == 2:

    st.markdown('<div class="eyebrow">BUSINESS SIGNALS</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Understand the opportunity space</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Review the commercial context before the agent ranks recommendations.</div>',
        unsafe_allow_html=True,
    )

    a, b, c, d = st.columns(4)
    with a:
        st.metric("Merchant", merchant_value("name"))
    with b:
        st.metric("Primary product", PRIMARY_PRODUCT)
    with c:
        st.metric("Orders", merchant_value("orders"))
    with d:
        st.metric("Candidate opportunities", "3")

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        with st.container(border=True):
            st.caption("CUSTOMER SIGNAL")
            st.subheader("Strong fitness intent")
            st.write("The customer profile supports adjacent fitness and nutrition purchases.")

    with right:
        with st.container(border=True):
            st.caption("PRODUCT SIGNAL")
            st.subheader("Complementary categories")
            st.write("Fitness accessories and nutrition add-ons create a credible cross-sell space.")

    st.info("Context signal · Customer, product and merchant relationships are ready for AI analysis.")

    if st.button("Run AI analysis  →", type="primary"):
        next_stage()

# ============================================================
# 04 AI ANALYSIS
# ============================================================

elif stage == 3:

    st.markdown('<div class="eyebrow">AI REASONING</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">How the agent evaluated the business</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">The agent evaluates customer fit, product relationships, purchase relevance and governance constraints.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([2.7, 1])

    with left:
        with st.container(border=True):
            rows = [
                ("Merchant context", "Loaded"),
                ("Customer profile", "Evaluated"),
                ("Product relationships", "Analyzed"),
                ("Opportunity candidates", "Ranked"),
                ("Policy constraints", "Checked"),
            ]
            for label, status in rows:
                st.markdown(
                    f"""
                    <div class="timeline-line">
                        <div class="timeline-dot">✓</div>
                        <div class="timeline-label">{label}</div>
                        <div class="timeline-status">{status}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    with right:
        with st.container(border=True):
            st.caption("AGENT RESULT")
            st.metric("Opportunities", "3")
            st.metric("Best recommendation", "92%")
            st.metric("Signal quality", "Strong")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="reason-box">
            <strong>Agent reasoning</strong><br>
            Fitness-focused customers purchasing the primary nutrition product
            show strong potential for adjacent workout and nutrition products.
            Higher-ranked opportunities are those where customer fit,
            category fit and purchase relevance reinforce each other.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Explore growth opportunities  →", type="primary"):
        next_stage()

# ============================================================
# 05 OPPORTUNITIES
# ============================================================

elif stage == 4:

    st.markdown('<div class="eyebrow">GROWTH INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Recommended opportunities</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Compare all three opportunities before selecting one for detailed review.</div>',
        unsafe_allow_html=True,
    )

    tabs = st.tabs(["Recommended", "Comparison", "Customer fit"])

    with tabs[0]:
        for i, product in enumerate(PRODUCTS):
            left, middle, right = st.columns([4.1, 1.45, 1])

            with left:
                with st.container(border=True):
                    st.caption(product["category"].upper())
                    st.subheader(product["name"])
                    st.caption(product["role"])
                    st.write(product["reason"])

            with middle:
                with st.container(border=True):
                    st.caption("FIT")
                    st.markdown(f'<div class="score-big">{product["score"]}%</div>', unsafe_allow_html=True)
                    st.caption("Recommendation")
                    st.markdown(
                        f'<div class="score-track"><div class="score-fill" style="width:{product["score"]}%"></div></div>',
                        unsafe_allow_html=True,
                    )

            with right:
                st.write("")
                if st.button("Review", key=f"review_{i}", type="primary"):
                    select_product(product)

    with tabs[1]:
        st.caption("OPPORTUNITY COMPARISON")
        for product in PRODUCTS:
            a, b, c, d = st.columns([2.4, 1, 1, 1])
            with a:
                st.write(f"**{product['name']}**")
            with b:
                st.metric("Fit", f"{product['score']}%")
            with c:
                st.metric("Impact", product["impact"])
            with d:
                st.metric("Confidence", product["confidence"])

    with tabs[2]:
        for product in PRODUCTS:
            with st.container(border=True):
                st.subheader(product["name"])
                a, b, c = st.columns(3)
                with a:
                    st.metric("Customer fit", f"{product['customer_fit']}%")
                with b:
                    st.metric("Category fit", f"{product['category_fit']}%")
                with c:
                    st.metric("Purchase relevance", f"{product['purchase_relevance']}%")

# ============================================================
# 06 REVIEW
# ============================================================

elif stage == 5:

    product = st.session_state.selected_product

    st.markdown('<div class="eyebrow">OPPORTUNITY REVIEW</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Why the agent recommends this</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Review the selected opportunity and the evidence supporting the recommendation.</div>',
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.caption("SELECTED OPPORTUNITY")
        st.subheader(f"{PRIMARY_PRODUCT} → {product['name']}")
        st.write(product["reason"])

        a, b, c = st.columns(3)
        with a:
            st.metric("Overall fit", f"{product['score']}%")
        with b:
            st.metric("Customer fit", f"{product['customer_fit']}%")
        with c:
            st.metric("Expected impact", product["impact"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">AI SCORING BREAKDOWN</div>', unsafe_allow_html=True)

    for label, score in [
        ("Customer fit", product["customer_fit"]),
        ("Category fit", product["category_fit"]),
        ("Purchase relevance", product["purchase_relevance"]),
    ]:
        a, b = st.columns([1.6, 5])
        with a:
            st.write(f"**{label}**")
        with b:
            st.markdown(
                f'<div class="score-track"><div class="score-fill" style="width:{score}%"></div></div>',
                unsafe_allow_html=True,
            )
            st.caption(f"{score}%")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">EVIDENCE</div>', unsafe_allow_html=True)

    for evidence in product["evidence"]:
        st.success(evidence)

    if st.button("Send recommendation to governance  →", type="primary"):
        next_stage()

# ============================================================
# 07 GOVERNANCE
# ============================================================

elif stage == 6:

    st.markdown('<div class="eyebrow">POLICY CONTROL</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Governance validation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">The proposed recommendation must pass policy and approval checks before controlled action.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([2.7, 1])

    with left:
        with st.container(border=True):
            checks = [
                "Merchant decision",
                "Recommendation validity",
                "Policy compliance",
                "Approval requirement",
                "Execution boundary",
            ]
            for check in checks:
                st.markdown(
                    f"""
                    <div class="timeline-line">
                        <div class="timeline-dot">✓</div>
                        <div class="timeline-label">{check}</div>
                        <div class="timeline-status">Passed</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    with right:
        with st.container(border=True):
            st.caption("POLICY STATUS")
            st.subheader("Ready")
            st.write("All required checks have passed.")
            st.success("Governance passed")

    st.markdown(
        """
        <div class="reason-box">
            <strong>Control principle</strong><br>
            The AI agent may identify and rank opportunities, but an action remains
            non-executable until it satisfies the independent governance boundary.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Continue to decision checkpoint  →", type="primary"):
        next_stage()

# ============================================================
# 08 APPROVAL
# ============================================================

elif stage == 7:

    product = st.session_state.selected_product

    st.markdown('<div class="eyebrow">DECISION CHECKPOINT</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Review before action</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Confirm the exact recommendation and safety boundary before processing.</div>',
        unsafe_allow_html=True,
    )

    a, b = st.columns(2)

    with a:
        with st.container(border=True):
            st.caption("PROPOSED DECISION")
            st.subheader(f"{PRIMARY_PRODUCT} → {product['name']}")
            st.write(product["reason"])
            st.metric("Recommendation fit", f"{product['score']}%")

    with b:
        with st.container(border=True):
            st.caption("CONTROL BOUNDARY")
            st.write("Approval required")
            st.write("Controlled simulation")
            st.write("External merchant changes disabled")

    st.warning(
        "Approval advances the controlled workflow only. External merchant state remains unchanged."
    )

    if st.button("Approve simulated action  →", type="primary"):
        next_stage()

# ============================================================
# 09 EXECUTION
# ============================================================

elif stage == 8:

    st.markdown('<div class="eyebrow">CONTROLLED ACTION</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Processing approved decision</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">The workflow advances through a controlled action pipeline inside the simulation boundary.</div>',
        unsafe_allow_html=True,
    )

    pipeline = [
        ("01", "Recommendation accepted", "Complete"),
        ("02", "Governance validated", "Complete"),
        ("03", "Authorization confirmed", "Complete"),
        ("04", "Action processed", "Simulated"),
    ]

    with st.container(border=True):
        for number, label, status in pipeline:
            st.markdown(
                f"""
                <div class="timeline-line">
                    <div class="timeline-dot">{number}</div>
                    <div class="timeline-label">{label}</div>
                    <div class="timeline-status">{status}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.info("Controlled simulation · The action lifecycle is represented without making an external system call.")

    if st.button("Run verification  →", type="primary"):
        next_stage()

# ============================================================
# 10 VERIFICATION
# ============================================================

elif stage == 9:

    st.markdown('<div class="eyebrow">ASSURANCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Verification complete</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">The assurance layer confirms the action remains consistent with the approved decision path.</div>',
        unsafe_allow_html=True,
    )

    a, b, c = st.columns(3)
    with a:
        st.metric("Decision consistency", "Passed")
    with b:
        st.metric("Policy consistency", "Passed")
    with c:
        st.metric("External change", "None")

    with st.container(border=True):
        st.caption("ASSURANCE CHECKS")
        for item in [
            "Approved recommendation matches processed action",
            "Authorization path remains intact",
            "Action stayed within simulation boundary",
            "Result is suitable for audit",
        ]:
            st.success(item)

    if st.button("View outcome  →", type="primary"):
        next_stage()

# ============================================================
# 11 OUTCOME
# ============================================================

elif stage == 10:

    product = st.session_state.selected_product

    st.markdown('<div class="eyebrow">RESULT</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Decision outcome</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">Review the result produced by the governed workflow.</div>',
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.caption("COMPLETED OPPORTUNITY")
        st.subheader(f"{PRIMARY_PRODUCT} → {product['name']}")
        st.write("The recommendation completed the controlled simulation lifecycle.")

    a, b, c = st.columns(3)
    with a:
        st.metric("Decision", "Approved")
    with b:
        st.metric("Verification", "Passed")
    with c:
        st.metric("External change", "None")

    st.success("Outcome verified. The decision can be recorded in the audit trail.")

    if st.button("Open audit trail  →", type="primary"):
        next_stage()

# ============================================================
# 12 AUDIT
# ============================================================

elif stage == 11:

    st.markdown('<div class="eyebrow">TRACEABILITY</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Decision audit trail</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">A concise record of the governed decision journey.</div>',
        unsafe_allow_html=True,
    )

    events = [
        "Business context established",
        "Customer and product signals analyzed",
        "Growth opportunities ranked",
        "Recommendation evidence reviewed",
        "Governance validation passed",
        "Approval checkpoint completed",
        "Controlled action processed",
        "Verification completed",
        "Outcome recorded",
    ]

    with st.container(border=True):
        for i, event in enumerate(events, 1):
            st.markdown(
                f"""
                <div class="timeline-line">
                    <div class="timeline-dot">{i:02d}</div>
                    <div class="timeline-label">{event}</div>
                    <div class="timeline-status">Recorded</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.info("Audit trail recorded for review within the controlled simulation.")

    if st.button("View executive summary  →", type="primary"):
        next_stage()

# ============================================================
# 13 EXECUTIVE SUMMARY
# ============================================================

elif stage == 12:

    product = st.session_state.selected_product
    rank = 1 if product["score"] == 92 else 2 if product["score"] == 87 else 3

    st.markdown('<div class="eyebrow">EXECUTIVE VIEW</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Decision summary</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-copy">A business-facing summary of what the agent recommended, why it was selected and how the workflow ended.</div>',
        unsafe_allow_html=True,
    )

    st.success(
        "Workflow complete. Analysis, governance, approval, controlled action, verification and audit all completed."
    )

    with st.container(border=True):
        st.caption("FINAL DECISION")
        st.subheader(f"{PRIMARY_PRODUCT} → {product['name']}")
        st.write(product["reason"])

        a, b, c = st.columns(3)
        with a:
            st.metric("Recommendation fit", f"{product['score']}%")
        with b:
            st.metric("Expected impact", product["impact"])
        with c:
            st.metric("Opportunity rank", f"{rank} of 3")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">BUSINESS CONTEXT</div>', unsafe_allow_html=True)

    a, b, c, d = st.columns(4)
    with a:
        st.metric("Merchant", merchant_value("name"))
    with b:
        st.metric("Customer profile", "Fitness focused")
    with c:
        st.metric("Primary product", PRIMARY_PRODUCT)
    with d:
        st.metric("External changes", "None")

    st.markdown("<br>", unsafe_allow_html=True)

    a, b = st.columns(2)

    with a:
        with st.container(border=True):
            st.caption("WHY THIS OPPORTUNITY")
            st.write(
                f"Customer fit: {product['customer_fit']}% · "
                f"Category fit: {product['category_fit']}% · "
                f"Purchase relevance: {product['purchase_relevance']}%"
            )
            st.markdown(
                f'<div class="score-track"><div class="score-fill" style="width:{product["score"]}%"></div></div>',
                unsafe_allow_html=True,
            )

    with b:
        with st.container(border=True):
            st.caption("WORKFLOW ASSURANCE")
            st.write("Governance · Passed")
            st.write("Verification · Passed")
            st.write("Audit · Recorded")

    st.warning("Controlled simulation · No external merchant system or merchant state was modified.")

    if st.button("Start new analysis", type="primary"):
        reset_workflow()

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="app-footer">
        <span>Governed AI Work Agent · Decision intelligence</span>
        <span>Controlled simulation · Audit ready</span>
    </div>
    """,
    unsafe_allow_html=True,
)
