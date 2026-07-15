import streamlit as st
from pages.common import notice


def render():
    st.title("Methodology, Transparency & Limitations")
    st.markdown("### How the simulator works\n1. You enter non-sensitive income, expense, savings, goal and purchase values.\n2. Deterministic formulas calculate each option.\n3. The app compares underlying metrics rather than calling one option universally best.\n4. What-if and stress tests change stated assumptions and recalculate.")
    st.markdown("### Assumptions\nWhere relevant, the model may hold income, expenses, interest rates, purchase price, and monthly savings constant. Waiting-price changes and hypothetical growth are explicitly entered assumptions. Actual outcomes may differ because of inflation, taxes, changing prices, emergencies, or other circumstances.")
    st.markdown("### Limitations\nIt does not model every tax, product-quality, family, health, or career factor; predict markets; access bank systems; or guarantee outcomes. A lower monetary cost may not mean a better personal choice.")
    st.markdown("### Privacy\nSession-only values disappear when the session ends. Never enter bank account/card details, CVVs, PINs, OTPs, passwords, Aadhaar, PAN, or login credentials.")
    notice()
