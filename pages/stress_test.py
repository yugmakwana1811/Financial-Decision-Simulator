import streamlit as st
import pandas as pd
from modules.stress_engine import PRESETS, apply_stress
from modules.consequence_engine import baseline
from pages.common import money, coverage, classification_note


def render(profile, results):
    st.title("Financial Stress Test")
    st.write("Apply hypothetical shocks after choosing one scenario. For EMI, the monthly EMI remains an obligation during the shock.")
    choice=st.selectbox("Decision to stress test",[r.name for r in results]); result=next(r for r in results if r.name==choice)
    shock_name=st.selectbox("Stress preset",list(PRESETS)+["Custom shock"])
    if shock_name=="Custom shock":
        a,b,c=st.columns(3); shock={"income_drop":a.number_input("Income fall %",0.0,100.0,0.0),"expense_rise":b.number_input("Essential-expense rise %",0.0,500.0,0.0),"unexpected":c.number_input("Unexpected one-time expense",0.0,step=1000.0)}
    else: shock=PRESETS[shock_name]
    stressed=apply_stress(profile,result,shock); base=baseline(profile)
    rows=[{"Stage":"Before decision","Savings":profile["savings"],"Monthly surplus":base["surplus"],"Emergency coverage":base["coverage"]},{"Stage":"After decision","Savings":result.savings_remaining,"Monthly surplus":result.monthly_surplus,"Emergency coverage":result.emergency_coverage},{"Stage":"After stress scenario","Savings":stressed["savings"],"Monthly surplus":stressed["surplus"],"Emergency coverage":stressed["coverage"]}]
    df=pd.DataFrame(rows); st.dataframe(df,hide_index=True,use_container_width=True)
    st.bar_chart(df.set_index("Stage")[["Savings","Monthly surplus"]])
    if stressed["surplus"]<0: st.warning("Under this hypothetical shock, the monthly result is a deficit. This is a resilience signal, not a prediction.")
    if stressed["coverage"] is None: st.warning("Coverage is not calculable because stressed essential expenses are zero.")
    classification_note()
