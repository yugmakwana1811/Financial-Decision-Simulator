import streamlit as st
from modules.charts import comparison_frame, scenario_cost_chart
from pages.common import money, coverage, classification_note


def render(results):
    st.title("Scenario Comparison")
    st.write("These are metric leaders under the current inputs, not universal recommendations.")
    df=comparison_frame(results)
    display=df[["name","immediate_payment","monthly_emi","total_cost","interest_paid","savings_remaining","monthly_surplus","emergency_coverage","goal_delay_months"]].copy()
    display.columns=["Scenario","Immediate payment","Monthly EMI","Total cost","Interest paid","Savings remaining","Monthly surplus / deficit","Emergency coverage (months)","Goal delay (months)"]
    st.dataframe(display, use_container_width=True, hide_index=True, column_config={c:st.column_config.NumberColumn(format="Rs. %,.0f") for c in ["Immediate payment","Monthly EMI","Total cost","Interest paid","Savings remaining","Monthly surplus / deficit"]})
    low=df.loc[df.total_cost.idxmin()]; liquid=df.loc[df.savings_remaining.idxmax()]; debt=df.loc[df.monthly_emi.idxmin()]
    st.markdown(f"- **Lowest total cost under current inputs:** {low['name']} ({money(low['total_cost'])})\n- **Highest immediate liquidity preserved:** {liquid['name']} ({money(liquid['savings_remaining'])})\n- **Lowest new debt commitment:** {debt['name']} ({money(debt['monthly_emi'])}/month)")
    st.plotly_chart(scenario_cost_chart(df),use_container_width=True)
    st.download_button("Export comparison CSV",df.to_csv(index=False).encode(),"scenario_comparison.csv","text/csv")
    classification_note()
