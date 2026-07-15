import streamlit as st
from modules.consequence_engine import build_scenarios
from modules.charts import comparison_frame, cashflow_chart
from pages.common import money, classification_note


def render(profile, purchase):
    st.title("What-If Laboratory")
    st.write("Change a few assumptions here without changing the main simulator inputs. All outputs recalculate immediately.")
    with st.form("whatif"):
        a,b,c=st.columns(3)
        price=a.number_input("Purchase price",0.0,value=float(purchase["price"]),step=1000.0)
        rate=b.number_input("Interest rate %",0.0,value=float(purchase["annual_rate"]),step=.5)
        down=c.number_input("Down payment",0.0,value=float(purchase["down_payment"]),step=1000.0)
        income_change=a.slider("Income change %",-50,50,0)
        essential_change=b.slider("Essential-expense change %",-50,100,0)
        tenure=c.number_input("EMI tenure",1,value=int(purchase["tenure"]),step=1)
        delay=a.number_input("Wait period",0,value=int(purchase["delay_months"]),step=1)
        alt=b.number_input("Alternative price",0.0,value=float(purchase["alternative_price"]),step=1000.0)
        growth=c.number_input("Hypothetical growth %",0.0,value=float(purchase["growth_rate"]),step=.5)
        submitted=st.form_submit_button("Run what-if simulation",type="primary")
    if submitted or "whatif_result" not in st.session_state:
        p=dict(profile); q=dict(purchase); p["primary_income"]*=1+income_change/100; p["essential"]*=1+essential_change/100
        q.update({"price":price,"annual_rate":rate,"down_payment":min(down,price),"tenure":tenure,"delay_months":delay,"alternative_price":alt,"growth_rate":growth})
        st.session_state.whatif_result=build_scenarios(p,q)
    df=comparison_frame(st.session_state.whatif_result)
    st.dataframe(df[["name","total_cost","monthly_emi","savings_remaining","monthly_surplus"]],hide_index=True,use_container_width=True)
    st.plotly_chart(cashflow_chart(df),use_container_width=True)
    st.caption("ASSUMPTION: This laboratory holds all non-edited entries constant. Results are conditional, not forecasts.")
    classification_note()
