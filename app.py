import streamlit as st

from modules.consequence_engine import build_scenarios
from pages import home, financial_profile, decision_simulator, scenario_comparison, what_if_lab, stress_test, visual_analytics, learn, methodology

st.set_page_config(page_title="Financial Decision Simulator", page_icon="📊", layout="wide")

DEFAULT_PROFILE={"primary_income":50000.0,"other_income":0.0,"essential":25000.0,"non_essential":8000.0,"savings":150000.0,"existing_debt":2000.0,"goal_name":"Higher education","goal_target":300000.0,"goal_current":20000.0,"goal_contribution":5000.0}
DEFAULT_PURCHASE={"description":"Laptop","price":60000.0,"down_payment":10000.0,"annual_rate":12.0,"tenure":12,"alternative_price":45000.0,"delay_months":6,"monthly_wait_saving":8000.0,"wait_price_change":0.0,"growth_rate":6.0,"opportunity_years":3.0}

def load_demo():
    st.session_state.profile=dict(DEFAULT_PROFILE); st.session_state.purchase=dict(DEFAULT_PURCHASE); st.session_state.results=build_scenarios(st.session_state.profile,st.session_state.purchase)

if "profile" not in st.session_state: load_demo()
profile=st.session_state.profile; purchase=st.session_state.purchase
st.sidebar.title("Decision Simulator")
if st.sidebar.button("Load official demo",use_container_width=True): load_demo(); st.rerun()
page=st.sidebar.radio("Navigate",["Home & Project Overview","Financial Profile","Decision Simulator","Scenario Comparison","Consequence Engine","What-If Laboratory","Financial Stress Test","Visual Analytics","Learn the Concepts","Methodology & Limitations"])

if page=="Home & Project Overview": home.render(load_demo)
elif page=="Financial Profile": financial_profile.render(profile)
elif page=="Decision Simulator": decision_simulator.render(profile,purchase)
else:
    results=build_scenarios(profile,purchase)
    if page=="Scenario Comparison": scenario_comparison.render(results)
    elif page=="Consequence Engine":
        st.title("Multidimensional Consequence Engine")
        st.write("The engine calculates every consequence using the same inputs and transparent formulas.")
        for result in results:
            with st.expander(result.name,expanded=result.name=="EMI"):
                st.write(result.notes)
                st.json({"Immediate liquidity":result.savings_remaining,"Monthly cash flow":result.monthly_surplus,"Total monetary cost":result.total_cost,"Interest burden":result.interest_paid,"Emergency coverage":result.emergency_coverage,"Goal delay months":result.goal_delay_months,"Hypothetical opportunity future value":result.opportunity_future_value})
        st.caption("CALCULATIONS are mathematical results. Opportunity future values are PROJECTIONS conditional on the entered growth-rate assumption.")
    elif page=="What-If Laboratory": what_if_lab.render(profile,purchase)
    elif page=="Financial Stress Test": stress_test.render(profile,results)
    elif page=="Visual Analytics": visual_analytics.render(profile,results)
    elif page=="Learn the Concepts": learn.render()
    elif page=="Methodology & Limitations": methodology.render()
