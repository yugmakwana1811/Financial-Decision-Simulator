import streamlit as st
from modules.consequence_engine import baseline
from modules.validations import validate_profile
from pages.common import money, coverage, classification_note


def render(profile):
    st.title("Financial Profile")
    st.write("Enter recurring, non-sensitive figures. Inputs remain only in this browser session.")
    c1,c2=st.columns(2)
    with c1:
        profile["primary_income"] = st.number_input("Monthly primary income (INPUT)", min_value=0.0, value=float(profile["primary_income"]), step=1000.0)
        profile["other_income"] = st.number_input("Other recurring monthly income (INPUT)", min_value=0.0, value=float(profile["other_income"]), step=500.0)
        profile["essential"] = st.number_input("Essential monthly expenses (INPUT)", min_value=0.0, value=float(profile["essential"]), step=500.0, help="Housing, food, transport, education, utilities, and routine healthcare.")
        profile["non_essential"] = st.number_input("Non-essential monthly expenses (INPUT)", min_value=0.0, value=float(profile["non_essential"]), step=500.0, help="Entertainment, shopping, subscriptions, dining, and similar spending.")
    with c2:
        profile["savings"] = st.number_input("Available savings / emergency fund (INPUT)", min_value=0.0, value=float(profile["savings"]), step=1000.0)
        profile["existing_debt"] = st.number_input("Existing monthly EMI and debt payments (INPUT)", min_value=0.0, value=float(profile["existing_debt"]), step=500.0)
        profile["goal_name"] = st.text_input("Optional financial goal name", value=profile.get("goal_name", "Education fund"))
        profile["goal_target"] = st.number_input("Optional goal target amount", min_value=0.0, value=float(profile.get("goal_target",0)), step=1000.0)
        profile["goal_current"] = st.number_input("Current amount saved for goal", min_value=0.0, value=float(profile.get("goal_current",0)), step=1000.0)
        profile["goal_contribution"] = st.number_input("Monthly goal contribution (INPUT)", min_value=0.0, value=float(profile.get("goal_contribution",0)), step=500.0)
        profile["goal_target_date"] = st.text_input("Optional goal target date", value=profile.get("goal_target_date", ""), placeholder="e.g., December 2028")
    with st.expander("Optional expense detail (for learning and discussion)"):
        st.caption("These details are optional. Their total is not added again because the essential and non-essential totals above are used in calculations.")
        detail_names = ["Housing", "Food", "Transport", "Education", "Utilities", "Routine healthcare", "Entertainment", "Shopping", "Subscriptions", "Dining", "Other"]
        cols = st.columns(2)
        for index, name in enumerate(detail_names):
            key = f"detail_{name.lower().replace(' ', '_')}"
            profile[key] = cols[index % 2].number_input(name, min_value=0.0, value=float(profile.get(key, 0)), step=100.0, key=key)
    for error in validate_profile(profile): st.error(error)
    base=baseline(profile)
    st.markdown("### Baseline calculations")
    a,b,c=st.columns(3); a.metric("Total monthly income (CALCULATION)",money(base["income"])); b.metric("Monthly surplus / deficit (CALCULATION)",money(base["surplus"])); c.metric("Emergency coverage (CALCULATION)",coverage(base["coverage"]))
    if base["surplus"]<0: st.warning("This profile has a monthly deficit: recurring expenses and debt exceed income.")
    if base["coverage"] is None: st.warning("Emergency coverage cannot be calculated because essential monthly expenses were entered as zero.")
    with st.expander("Formula used"):
        st.write("Monthly surplus = total monthly income - essential expenses - non-essential expenses - existing debt payments.")
        st.write("Emergency coverage = available emergency savings / essential monthly expenses.")
    classification_note()
