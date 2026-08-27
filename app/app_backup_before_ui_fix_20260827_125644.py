
import streamlit as st
import pickle
import os

st.set_page_config(
    page_title="Governed AI Work Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DATA
# ============================================================

MERCHANT = {
    "merchant_id": "MERCHANT_001",
    "merchant_name": "FitFuel Store"
}

PRIMARY_PRODUCT = "Protein Bar"

RECOMMENDATIONS = [
    {
        "id": "RECOMMENDATION_003",
        "product": "Shaker Bottle",
        "score": 92,
        "category": "Fitness Accessory",
        "reason": "Complementary product for customers purchasing Protein Bar.",
        "evidence": [
            "Protein Bar has strong purchase demand.",
            "Shaker Bottle is identified as complementary.",
            "Existing Shaker Bottle demand is observed."
        ]
    },
    {
        "id": "RECOMMENDATION_004",
        "product": "Protein Cookies",
        "score": 87,
        "category": "Nutrition",
        "reason": "Complementary nutrition product for Protein Bar customers.",
        "evidence": [
            "Same fitness/nutrition customer segment.",
            "Natural product-category complement.",
            "Suitable for cross-sell exploration."
        ]
    },
    {
        "id": "RECOMMENDATION_005",
        "product": "Gym Towel",
        "score": 81,
        "category": "Fitness Accessory",
        "reason": "Relevant fitness accessory for the merchant's customers.",
        "evidence": [
            "Relevant fitness customer context.",
            "Complementary accessory category.",
            "Suitable for merchant review."
        ]
    }
]

# ============================================================
# SESSION STATE
# ============================================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "selected_recommendation" not in st.session_state:
    st.session_state.selected_recommendation = None

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.hero {
    padding: 45px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1f2937 100%
    );
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #d1d5db;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 20px;
    background: #374151;
    margin-right: 8px;
    font-size: 13px;
}

.card {
    padding: 25px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.score {
    font-size: 30px;
    font-weight: 700;
}

.small {
    color: #6b7280;
    font-size: 14px;
}

.step {
    font-size: 13px;
    color: #6b7280;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# STEP INDICATOR
# ============================================================

steps = [
    "Welcome",
    "Merchant",
    "Context",
    "Analysis",
    "Recommendations",
    "Details",
    "Governance",
    "Review",
    "Execution",
    "Verification",
    "Outcome",
    "Audit",
    "Summary"
]

st.progress(
    (st.session_state.step + 1) / len(steps)
)

st.caption(
    f"Step {st.session_state.step + 1} of {len(steps)}  •  "
    f"{steps[st.session_state.step]}"
)

# ============================================================
# STEP 1 — WELCOME
# ============================================================

if st.session_state.step == 0:

    st.markdown("""
    <div class="hero">
        <div class="badge">AI AGENT</div>
        <div class="badge">RAG</div>
        <div class="badge">GOVERNANCE</div>
        <div class="badge">SIMULATION</div>

        <h1>Governed AI Work Agent</h1>

        <p>
        AI-powered merchant growth decisions with
        governance, authorization, verification and auditability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("What this system does")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 🤖 AI Analysis")
        st.write(
            "Understands merchant context and identifies "
            "growth opportunities."
        )

    with c2:
        st.markdown("### 🛡️ Governance")
        st.write(
            "Every proposed action passes through "
            "the authoritative governance layer."
        )

    with c3:
        st.markdown("### 🔎 Auditability")
        st.write(
            "Tracks authorization, execution, verification "
            "and final outcome."
        )

    st.warning(
        "SIMULATION MODE — No external systems will be modified."
    )

    if st.button("Get Started →", type="primary"):
        st.session_state.step = 1
        st.rerun()

# ============================================================
# STEP 2 — MERCHANT
# ============================================================

elif st.session_state.step == 1:

    st.markdown("## Choose Merchant")
    st.write("Select the merchant whose business context you want to analyze.")

    st.markdown("""
    <div class="card">
        <h2>🏪 FitFuel Store</h2>
        <p class="small">
        Fitness & Nutrition Merchant
        </p>
        <p>
        Merchant ID: MERCHANT_001
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Select FitFuel Store →", type="primary"):
        st.session_state.step = 2
        st.rerun()

# ============================================================
# STEP 3 — BUSINESS CONTEXT
# ============================================================

elif st.session_state.step == 2:

    st.markdown("## Business Context")

    st.metric(
        "Merchant",
        "FitFuel Store"
    )

    st.subheader("Current Product Signals")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Protein Bar Orders", "150")

    with c2:
        st.metric("Shaker Bottle Orders", "45")

    with c3:
        st.metric("Detected Opportunities", "3")

    st.info(
        "The system will use this context to identify "
        "potential cross-sell opportunities."
    )

    if st.button("Analyze Business →", type="primary"):
        st.session_state.step = 3
        st.rerun()

# ============================================================
# STEP 4 — ANALYSIS
# ============================================================

elif st.session_state.step == 3:

    st.markdown("## AI Agent Analysis")

    st.write("The agent is analyzing the merchant context.")

    checks = [
        "Merchant context loaded",
        "Relevant business signals retrieved",
        "Products analyzed",
        "Growth opportunities identified",
        "Governance constraints checked"
    ]

    for item in checks:
        st.success("✓ " + item)

    st.metric(
        "Opportunities Found",
        len(RECOMMENDATIONS)
    )

    if st.button("View Recommendations →", type="primary"):
        st.session_state.step = 4
        st.rerun()

# ============================================================
# STEP 5 — MULTIPLE RECOMMENDATIONS
# ============================================================

elif st.session_state.step == 4:

    st.markdown("## AI Growth Opportunities")

    st.write(
        "The agent identified multiple potential products "
        "for cross-sell consideration."
    )

    for rec in RECOMMENDATIONS:

        st.markdown(
            f"""
            <div class="card">
                <div class="step">{rec["id"]}</div>
                <h2>{rec["product"]}</h2>
                <p class="small">{rec["category"]}</p>
                <p>{rec["reason"]}</p>
                <div class="score">{rec["score"]}%</div>
                <div class="small">Relevance score</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"View {rec['product']} →",
            key=rec["id"]
        ):
            st.session_state.selected_recommendation = rec
            st.session_state.step = 5
            st.rerun()

# ============================================================
# STEP 6 — DETAILS
# ============================================================

elif st.session_state.step == 5:

    rec = st.session_state.selected_recommendation

    st.markdown("## Recommendation Details")

    if rec:

        st.markdown(
            f"""
            <div class="card">
                <div class="step">{rec["id"]}</div>
                <h1>{PRIMARY_PRODUCT} → {rec["product"]}</h1>
                <p>{rec["reason"]}</p>
                <div class="score">{rec["score"]}%</div>
                <div class="small">Relevance</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Evidence")

        for evidence in rec["evidence"]:
            st.success("✓ " + evidence)

    if st.button("Request Governed Action →", type="primary"):
        st.session_state.step = 6
        st.rerun()

# ============================================================
# STEP 7 — GOVERNANCE
# ============================================================

elif st.session_state.step == 6:

    st.markdown("## Governance Check")

    checks = [
        ("Merchant decision", True),
        ("Recommendation validated", True),
        ("MODULE_23 authority", True),
        ("Governance handoff", True),
        ("Authorization required", True)
    ]

    for name, passed in checks:
        if passed:
            st.success("✓ " + name)

    st.info(
        "**Authoritative Governance Source: MODULE_23**"
    )

    if st.button("Continue to Action Review →", type="primary"):
        st.session_state.step = 7
        st.rerun()

# ============================================================
# STEP 8 — REVIEW
# ============================================================

elif st.session_state.step == 7:

    rec = st.session_state.selected_recommendation

    st.markdown("## Action Review")

    st.markdown(
        f"""
        <div class="card">
            <h3>Merchant</h3>
            <p>FitFuel Store</p>

            <h3>Opportunity</h3>
            <p>Protein Bar → {rec["product"]}</p>

            <h3>Recommendation</h3>
            <p>{rec["id"]}</p>

            <h3>Governance</h3>
            <p>MODULE_23 ✓</p>

            <h3>Execution</h3>
            <p>SIMULATION ONLY</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Approve Action →", type="primary"):
        st.session_state.step = 8
        st.rerun()

# ============================================================
# STEP 9 — EXECUTION
# ============================================================

elif st.session_state.step == 8:

    st.markdown("## Execution")

    lifecycle = [
        "Recommendation",
        "Governance",
        "Authorization",
        "Execution"
    ]

    for item in lifecycle:
        st.success("✓ " + item)

    st.warning(
        "Simulation Mode — external execution is disabled."
    )

    if st.button("Continue to Verification →", type="primary"):
        st.session_state.step = 9
        st.rerun()

# ============================================================
# STEP 10 — VERIFICATION
# ============================================================

elif st.session_state.step == 9:

    st.markdown("## Verification")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Execution", "EXECUTION_004")

    with c2:
        st.metric(
            "Verification",
            "VERIFICATION_RESPONSE_003"
        )

    with c3:
        st.metric("Authority", "MODULE_23")

    st.success("✓ Verification passed")

    if st.button("View Outcome →", type="primary"):
        st.session_state.step = 10
        st.rerun()

# ============================================================
# STEP 11 — OUTCOME
# ============================================================

elif st.session_state.step == 10:

    st.markdown("## Action Outcome")

    st.success(
        "✓ Workflow successfully processed in simulation."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Execution", "EXECUTION_004")

    with c2:
        st.metric("Outcome", "OUTCOME_003")

    with c3:
        st.metric("Authority", "MODULE_23")

    if st.button("View Audit Trail →", type="primary"):
        st.session_state.step = 11
        st.rerun()

# ============================================================
# STEP 12 — AUDIT
# ============================================================

elif st.session_state.step == 11:

    st.markdown("## Audit Trail")

    events = [
        "Recommendation created",
        "Governance validated",
        "Authorization validated",
        "Execution processed",
        "Verification completed",
        "Outcome generated"
    ]

    for event in events:
        st.success("✓ " + event)

    st.info("Audit ID: AUDIT_004")

    if st.button("View Final Summary →", type="primary"):
        st.session_state.step = 12
        st.rerun()

# ============================================================
# STEP 13 — SUMMARY
# ============================================================

elif st.session_state.step == 12:

    rec = st.session_state.selected_recommendation

    st.markdown(
        """
        <div class="hero">
            <h1>Workflow Complete ✓</h1>
            <p>Governed AI Work Agent</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Final Decision")

    st.write("**Merchant:** FitFuel Store")
    st.write(
        f"**Opportunity:** Protein Bar → {rec['product']}"
    )
    st.write(
        f"**Recommendation:** {rec['id']}"
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Governance", "MODULE_23")

    with c2:
        st.metric("Execution", "EXECUTION_004")

    with c3:
        st.metric("Audit", "AUDIT_004")

    st.success(
        "✓ All governed workflow stages completed."
    )

    st.warning(
        "SIMULATION MODE — No external system was modified."
    )

    if st.button("Start New Workflow"):
        st.session_state.step = 0
        st.session_state.selected_recommendation = None
        st.rerun()
