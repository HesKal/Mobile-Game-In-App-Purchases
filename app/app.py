from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "model.joblib"
LABELS = ["Minnow", "Dolphin", "Whale"]
FEATURE_COLS = ["Age", "Country", "Device", "GameGenre", "SessionCount", "AverageSessionLength"]

st.set_page_config(
    page_title="NovaPlay | Player Segment Studio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#f3f5fb; --muted:#a6afc5; --panel:#151c2d; --panel2:#1b2438; --line:#2a3550; --mint:#75f0c2; --violet:#a48bff; }
.stApp { background: radial-gradient(ellipse at 10% 0%, #182546 0%, #0b1020 48%, #090d18 100%); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width: 1220px; padding-top:2rem; padding-bottom:3rem; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; letter-spacing:-.025em; }
.hero { border:1px solid #2a3550; border-radius:24px; padding:28px 32px; background:linear-gradient(115deg,rgba(26,38,64,.96),rgba(19,26,43,.94)); box-shadow:0 16px 50px rgba(0,0,0,.18); margin-bottom:22px; }
.eyebrow { color:var(--mint); font-weight:700; letter-spacing:.13em; text-transform:uppercase; font-size:.72rem; }
.hero h1 { font-size:2.15rem; margin:.35rem 0 .35rem; color:#fff; }
.hero p { color:#bdc7da; font-size:1rem; margin:0; max-width:820px; }
.panel { border:1px solid var(--line); border-radius:18px; padding:20px 22px; background:rgba(21,28,45,.88); min-height:116px; }
.panel-label { color:var(--muted); font-size:.78rem; text-transform:uppercase; letter-spacing:.09em; font-weight:700; }
.panel-value { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:1.45rem; font-weight:700; margin-top:8px; }
.segment { border:1px solid rgba(117,240,194,.35); border-radius:20px; padding:26px; background:linear-gradient(140deg,rgba(117,240,194,.12),rgba(164,139,255,.12)); }
.segment h2 { font-size:2rem; margin:.3rem 0; color:#fff; }
.small { color:var(--muted); font-size:.9rem; }
div[data-testid="stForm"] { border:1px solid var(--line); border-radius:18px; padding:20px 22px; background:rgba(21,28,45,.9); }
.stButton>button,div[data-testid="stFormSubmitButton"] button { border:0; border-radius:12px; color:#08131c; font-weight:800; background:linear-gradient(90deg,#75f0c2,#96e9e2); padding:.62rem 1.1rem; }
.stButton>button:hover,div[data-testid="stFormSubmitButton"] button:hover { color:#08131c; border:0; filter:brightness(1.06); }
[data-testid="stSidebar"] { background:#111827; border-right:1px solid var(--line); }
hr { border-color:var(--line); }
[data-testid="stMetric"] { background:rgba(21,28,45,.8); padding:14px 16px; border:1px solid var(--line); border-radius:14px; }
div[data-testid="stAlert"] { border-radius:14px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("model.joblib is missing. Run train_model.py before starting the app.")
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except Exception as exc:
    st.error(f"The prediction model could not be loaded: {exc}")
    st.stop()

st.markdown("""
<div class="hero">
  <div class="eyebrow">NOVAPLAY STUDIOS · PLAYER INTELLIGENCE</div>
  <h1>Player Segment Studio</h1>
  <p>Explore how a player profile is classified, then consider a segment-specific promotion idea to test. Predictions are decision support—not a guarantee of spending or campaign impact.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### NovaPlay")
    st.caption("SEGMENT CLASSIFICATION · MODEL DEMO")
    st.markdown("---")
    st.markdown("**How to use**")
    st.write("Enter the six profile and gameplay fields, then choose **Predict segment**.")
    st.markdown("---")
    st.markdown("**Model**")
    st.write("Gini Decision Tree")
    st.write("Six profile/session predictors")
    st.markdown("---")
    st.caption("Training data are synthetic/expanded project data. Do not use this demo to make live player decisions.")

country_options = [
    "Australia", "Bangladesh", "Brazil", "Canada", "China", "Denmark", "Egypt", "France", "Germany", "India", "Iran", "Italy", "Japan", "Mexico", "Netherlands", "Norway", "Russia", "Saudi Arabia", "South Korea", "Spain", "Sri Lanka", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United States", "Afghanistan", "Unknown"
]
genre_options = ["Action RPG", "Adventure", "Battle Royale", "Card", "Casual", "Fighting", "MMORPG", "MOBA", "Puzzle", "Racing", "Role Playing", "Sandbox", "Simulation", "Sports", "Strategy", "Unknown"]

col_form, col_side = st.columns([1.15, .85], gap="large")
with col_form:
    st.subheader("Player profile")
    st.write("Use the profile information available at the intended prediction time.")
    with st.form("player_profile", clear_on_submit=False):
        a, b = st.columns(2)
        with a:
            age = st.number_input("Age", min_value=13, max_value=100, value=30, step=1, help="Enter an age from 13 to 100.")
            country = st.selectbox("Country", country_options, index=country_options.index("United States"))
            device = st.selectbox("Device", ["Android", "iOS", "Unknown"])
        with b:
            genre = st.selectbox("Favourite game genre", genre_options, index=genre_options.index("Adventure"))
            sessions = st.number_input("Session count", min_value=0, max_value=500, value=10, step=1, help="Number of sessions in the selected observation period.")
            avg_length = st.number_input("Average session length (minutes)", min_value=0.0, max_value=600.0, value=20.0, step=1.0, help="Use a non-negative value in minutes.")
        submitted = st.form_submit_button("Predict player segment", use_container_width=True)

with col_side:
    st.subheader("What the model uses")
    st.markdown("""
    <div class="panel">
      <div class="panel-label">Input signals</div>
      <div class="panel-value">Profile + engagement</div>
      <div class="small">Age, country, device, game genre, session count and average session length.</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("Direct spending amounts and generated 30-day helper fields are not entered, to reduce target leakage and keep the demo focused on the selected predictor set.")

if submitted:
    if avg_length < 0:
        st.error("Average session length cannot be negative.")
        st.stop()
    record = pd.DataFrame([{
        "Age": float(age),
        "Country": str(country),
        "Device": str(device),
        "GameGenre": str(genre),
        "SessionCount": float(sessions),
        "AverageSessionLength": float(avg_length),
    }], columns=FEATURE_COLS)
    prediction = str(model.predict(record)[0])
    probabilities = model.predict_proba(record)[0]
    classes = list(model.named_steps["model"].classes_)
    scores = {str(label): float(prob) for label, prob in zip(classes, probabilities)}
    score = scores.get(prediction, 0.0)

    st.markdown("---")
    st.subheader("Prediction")
    result_left, result_right = st.columns([1, 1], gap="large")
    with result_left:
        st.markdown(f"""
        <div class="segment">
          <div class="eyebrow">PREDICTED SPENDING SEGMENT</div>
          <h2>{prediction}</h2>
          <div class="small">Model score for this predicted class: {score:.1%}. This score is not a guarantee of the player's future spending.</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown("**Class scores**")
        st.bar_chart(pd.DataFrame({"Model score": [scores.get(label, 0.0) for label in LABELS]}, index=LABELS), horizontal=True, height=190, color="#75f0c2")
    with result_right:
        st.markdown("**Illustrative promotion idea to test**")
        ideas = {
            "Minnow": ("Low-commitment introduction", "Test an optional, low-price starter bundle. Measure incremental conversion and contribution margin, and monitor retention."),
            "Dolphin": ("Mid-tier value offer", "Test a time-limited value bundle or loyalty reward. Compare purchase lift and margin with a holdout group."),
            "Whale": ("Premium experience", "Test a premium bundle or VIP-style benefit with clear value. Monitor incremental margin and player retention."),
        }
        title, desc = ideas[prediction]
        st.markdown(f"""
        <div class="panel">
          <div class="panel-label">HYPOTHESIS · NOT A PROVEN RECOMMENDATION</div>
          <div class="panel-value">{title}</div>
          <div class="small">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.caption("Business check: compare the offer with a holdout group using incremental IAP revenue, contribution margin, conversion and retention.")

    st.markdown("#### Why did the model predict this?")
    st.write("The chart below shows the features the fitted tree relied on most across all training examples. These are associations used by the model; they do not show that a feature causes spending.")
    preprocessor = model.named_steps["preprocess"]
    estimator = model.named_steps["model"]
    names = preprocessor.get_feature_names_out()
    raw_importances = pd.Series(estimator.feature_importances_, index=names)
    aggregated = {}
    for name, importance in raw_importances.items():
        if name.startswith("numeric__"):
            base = name.split("__", 1)[1]
        elif name.startswith("categorical__"):
            base = name.split("__", 1)[1].split("_", 1)[0]
        else:
            base = name
        aggregated[base] = aggregated.get(base, 0.0) + float(importance)
    importance = pd.Series(aggregated).sort_values(ascending=True).tail(6)
    st.bar_chart(importance, horizontal=True, height=250, color="#a48bff")
    st.caption("Feature importance is a global summary of how the tree made its splits. It is not causal evidence and does not explain this individual prediction on its own.")

    with st.expander("View the player inputs used"):
        st.dataframe(record, hide_index=True, use_container_width=True)

st.markdown("---")
st.markdown("#### Project evaluation reference")
m1, m2, m3, m4 = st.columns(4)
for col, label, value in [
    (m1, "Test accuracy", "94.62%"),
    (m2, "Balanced accuracy", "86.23%"),
    (m3, "Macro-F1", "86.65%"),
    (m4, "Whale precision", "81.05%"),
]:
    with col:
        st.metric(label, value)
st.caption("These are the team's reported held-out test results for the Gini Decision Tree. They describe the project dataset, not guaranteed performance on live NovaPlay players.")

with st.expander("What this demo can—and cannot—show"):
    st.write("This app demonstrates how a player profile can be assigned to a spending segment and how that segment might inform a promotion experiment. It does not estimate how much the player will spend, determine the best offer, or prove that a promotion will increase revenue. A real campaign decision should be tested against a holdout group and assessed using incremental revenue, contribution margin, conversion and retention.")

st.caption("NovaPlay Studios · Academic project demonstration · Model: Gini Decision Tree")
