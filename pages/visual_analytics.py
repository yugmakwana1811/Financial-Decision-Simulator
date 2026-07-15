import streamlit as st
from modules.charts import comparison_frame, coverage_chart, cashflow_chart, emi_breakdown, savings_timeline


def render(profile, results):
    st.title("Visual Analytics")
    st.write("Every chart is drawn from the same scenario calculations used in the comparison table.")
    df=comparison_frame(results)
    a,b=st.columns(2); a.plotly_chart(coverage_chart(df),use_container_width=True); b.plotly_chart(cashflow_chart(df),use_container_width=True)
    st.plotly_chart(savings_timeline(profile,results),use_container_width=True)
    emi_result=next(x for x in results if x.name=="EMI")
    st.plotly_chart(emi_breakdown(emi_result),use_container_width=True)
    st.caption("Savings path is a PROJECTION under a constant-income, constant-expense, constant-EMI assumption. It does not predict actual future savings.")
