from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional

from modules.calculations import emergency_coverage, emi, future_value, goal_delay, monthly_surplus, total_repayment


@dataclass
class ScenarioResult:
    name: str
    immediate_payment: float
    monthly_emi: float
    total_cost: float
    interest_paid: float
    savings_remaining: float
    monthly_surplus: float
    emergency_coverage: Optional[float]
    goal_delay_months: Optional[float]
    opportunity_future_value: float
    notes: str

    def row(self) -> dict:
        return asdict(self)


def baseline(profile: dict) -> dict:
    income = profile["primary_income"] + profile.get("other_income", 0)
    surplus = monthly_surplus(income, profile["essential"], profile["non_essential"], profile.get("existing_debt", 0))
    return {"income": income, "surplus": surplus, "coverage": emergency_coverage(profile["savings"], profile["essential"])}


def build_scenarios(profile: dict, purchase: dict) -> list[ScenarioResult]:
    base = baseline(profile)
    savings, essential = profile["savings"], profile["essential"]
    goal_contribution = profile.get("goal_contribution", 0)
    rate, years = purchase.get("growth_rate", 6.0), purchase.get("opportunity_years", 3.0)
    price = purchase["price"]
    cash_remaining = savings - price
    cash = ScenarioResult("Cash now", price, 0, price, 0, cash_remaining, base["surplus"], emergency_coverage(cash_remaining, essential), goal_delay(price, goal_contribution), future_value(price, rate, years), "Pays the full price today; no financing interest.")
    principal = price - purchase["down_payment"]
    monthly = emi(principal, purchase["annual_rate"], int(purchase["tenure"]))
    repayment = total_repayment(monthly, int(purchase["tenure"]))
    emi_remaining = savings - purchase["down_payment"]
    financed = ScenarioResult("EMI", purchase["down_payment"], monthly, purchase["down_payment"] + repayment, repayment-principal, emi_remaining, base["surplus"]-monthly, emergency_coverage(emi_remaining, essential), goal_delay(purchase["down_payment"], goal_contribution), future_value(purchase["down_payment"], rate, years), "EMI continues as a monthly obligation for the selected tenure.")
    delay = int(purchase["delay_months"])
    saved_while_waiting = purchase.get("monthly_wait_saving", 0) * delay
    assumed_price = price * (1 + purchase.get("wait_price_change", 0) / 100)
    wait_remaining = savings + saved_while_waiting - assumed_price
    wait = ScenarioResult("Wait & save", 0, 0, assumed_price, 0, wait_remaining, base["surplus"], emergency_coverage(wait_remaining, essential), goal_delay(assumed_price, goal_contribution), future_value(assumed_price, rate, years), f"Purchase price after waiting uses the entered assumption ({purchase.get('wait_price_change', 0):.1f}% change).")
    alt_price = purchase["alternative_price"]
    alt_remaining = savings - alt_price
    alternative = ScenarioResult("Lower-cost alternative", alt_price, 0, alt_price, 0, alt_remaining, base["surplus"], emergency_coverage(alt_remaining, essential), goal_delay(alt_price, goal_contribution), future_value(alt_price, rate, years), "Lower monetary cost does not assess quality, suitability, or other non-financial factors.")
    return [cash, financed, wait, alternative]
