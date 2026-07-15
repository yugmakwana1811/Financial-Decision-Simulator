from __future__ import annotations

from math import pow
from typing import Optional


def monthly_surplus(income: float, essential: float, non_essential: float, debt: float = 0) -> float:
    """Income remaining after recurring spending; a negative value is a deficit."""
    return income - essential - non_essential - debt


def emergency_coverage(savings: float, essential_expenses: float) -> Optional[float]:
    """Months of essentials covered, or None when essentials are zero."""
    return None if essential_expenses == 0 else savings / essential_expenses


def simple_interest(principal: float, annual_rate: float, years: float) -> float:
    return principal * annual_rate * years / 100


def compound_amount(principal: float, annual_rate: float, years: float, compounds_per_year: int = 1) -> float:
    return principal * pow(1 + annual_rate / (100 * compounds_per_year), compounds_per_year * years)


def emi(principal: float, annual_rate: float, months: int) -> float:
    if principal == 0:
        return 0.0
    if months <= 0:
        raise ValueError("EMI tenure must be a positive number of months.")
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if annual_rate == 0:
        return principal / months
    r = annual_rate / 1200
    return principal * (r * (1 + r) ** months) / ((1 + r) ** months - 1)


def total_repayment(monthly_emi: float, months: int) -> float:
    return monthly_emi * months


def future_value(principal: float, annual_rate: float, years: float) -> float:
    return principal * (1 + annual_rate / 100) ** years


def goal_delay(amount_diverted: float, monthly_contribution: float) -> Optional[float]:
    return None if monthly_contribution <= 0 else max(0.0, amount_diverted) / monthly_contribution
