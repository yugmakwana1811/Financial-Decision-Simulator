import streamlit as st
from pages.common import notice


def render(load_demo):
    st.title("Financial Decision Simulator")
    st.subheader("Understand the consequences before making the decision.")
    st.write("A local, transparent financial-literacy tool for comparing a cash purchase, EMI, waiting to save, and a lower-cost alternative.")
    a, b, c = st.columns(3)
    a.metric("Four choices", "Cash | EMI | Wait | Alternative")
    b.metric("Nine learning modules", "One connected simulator")
    c.metric("Data storage", "Session only")
    if st.button("Load official laptop demo", type="primary", use_container_width=True):
        load_demo(); st.success("Demo loaded. Open Financial Profile or Compare Scenarios.")
    st.markdown("### What this makes visible")
    st.markdown("- Liquidity, monthly cash flow, total cost, interest, emergency coverage, goal impact, opportunity-cost assumptions, and financial-shock resilience.\n- Transparent mathematics, not a black-box recommendation. You decide which trade-offs matter.")
    st.markdown("### Privacy")
    st.write("No login, cloud database, bank account number, card details, PIN, OTP, password, Aadhaar, PAN, or banking credentials are requested. Use fictional or non-sensitive figures.")
    notice()
