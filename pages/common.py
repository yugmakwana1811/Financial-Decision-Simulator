from __future__ import annotations

import streamlit as st


def money(value: float) -> str:
    return f"Rs. {value:,.0f}"


def coverage(value) -> str:
    return "Not calculable" if value is None else f"{value:.1f} months"


def classification_note() -> None:
    st.caption("Labels: INPUT = entered value | CALCULATION = formula result | ASSUMPTION = editable model value | PROJECTION = conditional future simulation")


def notice() -> None:
    st.info("Educational simulator only. Results depend on entered values and stated assumptions; they are not financial, investment, banking, legal, or tax advice.")
