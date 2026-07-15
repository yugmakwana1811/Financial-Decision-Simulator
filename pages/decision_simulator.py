import streamlit as st
from modules.consequence_engine import build_scenarios
from modules.validations import validate_purchase
from pages.common import money, coverage, classification_note


def render(profile, purchase):
    st.title("Major Purchase Decision Simulator")
    st.write("Model a proposed purchase, then view the four alternatives through the same transparent formulas.")
    l,r=st.columns(2)
    with l:
        purchase["description"] = st.text_input("Purchase description", purchase["description"])
        purchase["price"] = st.number_input("Purchase price (INPUT)", min_value=0.0, value=float(purchase["price"]), step=1000.0)
        purchase["down_payment"] = st.number_input("Planned down payment (INPUT)", min_value=0.0, value=float(purchase["down_payment"]), step=1000.0)
        purchase["annual_rate"] = st.number_input("Annual interest rate % (INPUT)", min_value=0.0, value=float(purchase["annual_rate"]), step=0.5)
        purchase["tenure"] = st.number_input("EMI tenure in months (INPUT)", min_value=1, value=int(purchase["tenure"]), step=1)
    with r:
        purchase["alternative_price"] = st.number_input("Lower-cost alternative price (INPUT)", min_value=0.0, value=float(purchase["alternative_price"]), step=1000.0)
        purchase["delay_months"] = st.number_input("Wait period in months (ASSUMPTION)", min_value=0, value=int(purchase["delay_months"]), step=1)
        purchase["monthly_wait_saving"] = st.number_input("Monthly saving while waiting (ASSUMPTION)", min_value=0.0, value=float(purchase["monthly_wait_saving"]), step=500.0)
        purchase["wait_price_change"] = st.number_input("Price change during wait % (ASSUMPTION)", value=float(purchase.get("wait_price_change",0)), step=1.0, help="Enter 0 if assuming the price stays unchanged.")
        purchase["growth_rate"] = st.number_input("Hypothetical annual growth % (ASSUMPTION)", min_value=0.0, value=float(purchase["growth_rate"]), step=0.5)
        purchase["opportunity_years"] = st.number_input("Opportunity-cost period in years (ASSUMPTION)", min_value=0.0, value=float(purchase["opportunity_years"]), step=0.5)
    errors=validate_purchase(purchase)
    if errors:
        for error in errors: st.error(error)
        return
    results=build_scenarios(profile,purchase); st.session_state.results=results
    tabs=st.tabs([x.name for x in results])
    for tab,result in zip(tabs,results):
        with tab:
            a,b,c,d=st.columns(4); a.metric("Savings remaining",money(result.savings_remaining)); b.metric("Monthly EMI",money(result.monthly_emi)); c.metric("Total cost",money(result.total_cost)); d.metric("Emergency coverage",coverage(result.emergency_coverage))
            st.write(result.notes)
            st.caption(f"CALCULATION: Interest paid {money(result.interest_paid)} | Goal delay {('not calculable: contribution is zero' if result.goal_delay_months is None else f'{result.goal_delay_months:.1f} months')} | PROJECTION: hypothetical future value of diverted amount {money(result.opportunity_future_value)} under {purchase['growth_rate']}% for {purchase['opportunity_years']} years.")
    classification_note()
