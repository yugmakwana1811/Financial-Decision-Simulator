from __future__ import annotations

from modules.calculations import emergency_coverage


PRESETS = {
    "Income decreases by 10%": {"income_drop": 10, "expense_rise": 0, "unexpected": 0},
    "Income decreases by 25%": {"income_drop": 25, "expense_rise": 0, "unexpected": 0},
    "Essential expenses increase by 15%": {"income_drop": 0, "expense_rise": 15, "unexpected": 0},
    "Unexpected expense of Rs. 25,000": {"income_drop": 0, "expense_rise": 0, "unexpected": 25000},
    "Unexpected expense of Rs. 50,000": {"income_drop": 0, "expense_rise": 0, "unexpected": 50000},
    "Combined: 20% income fall + Rs. 25,000 expense": {"income_drop": 20, "expense_rise": 0, "unexpected": 25000},
}


def apply_stress(profile: dict, scenario, shock: dict) -> dict:
    base_income = profile["primary_income"] + profile.get("other_income", 0)
    stressed_income = base_income * (1 - shock.get("income_drop", 0) / 100)
    stressed_essential = profile["essential"] * (1 + shock.get("expense_rise", 0) / 100)
    stressed_savings = scenario.savings_remaining - shock.get("unexpected", 0)
    stressed_surplus = stressed_income - stressed_essential - profile["non_essential"] - profile.get("existing_debt", 0) - scenario.monthly_emi
    return {"income": stressed_income, "essential": stressed_essential, "savings": stressed_savings, "surplus": stressed_surplus, "coverage": emergency_coverage(stressed_savings, stressed_essential)}
