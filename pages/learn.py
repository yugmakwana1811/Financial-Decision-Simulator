import streamlit as st


def render():
    st.title("Learn the Concepts")
    concepts={"Income":"Money received regularly.","Essential and non-essential expenditure":"Essentials support basic needs; non-essentials are more flexible spending.","Savings and emergency fund":"Savings kept aside; an emergency fund is available savings for essential costs during disruptions.","Surplus and deficit":"A surplus is income left after recurring costs. A deficit means recurring costs exceed income.","EMI, principal, rate and tenure":"An EMI is a monthly loan instalment. Principal is borrowed money; interest is its cost; tenure is the repayment period.","Total repayment and interest":"Total repayment is all EMIs paid. Interest is repayment minus principal.","Liquidity and resilience":"Liquidity is money readily available. Resilience is how the position responds to a hypothetical setback.","Opportunity cost":"A conditional comparison of what diverted money could become under a stated assumed growth rate.","Goals, assumptions and projections":"Goal delay is a simple estimate based on constant contributions. Assumptions are model choices; projections depend on them."}
    for title,text in concepts.items():
        with st.expander(title): st.write(text)
    st.markdown("### Core formulas")
    st.code("EMI = P × [r(1+r)^n] / [(1+r)^n − 1]\nFuture value = P × (1 + r)^t\nGoal delay = amount diverted / monthly goal contribution")
