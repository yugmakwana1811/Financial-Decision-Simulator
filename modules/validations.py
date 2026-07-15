from __future__ import annotations

from typing import Mapping


def validate_profile(profile: Mapping[str, float]) -> list[str]:
    errors = []
    for key in ("primary_income", "other_income", "essential", "non_essential", "savings", "existing_debt"):
        if profile.get(key, 0) < 0:
            errors.append(f"{key.replace('_', ' ').title()} cannot be negative.")
    if profile.get("goal_contribution", 0) < 0:
        errors.append("Monthly goal contribution cannot be negative.")
    return errors


def validate_purchase(purchase: Mapping[str, float]) -> list[str]:
    errors = []
    price = purchase.get("price", 0)
    if price <= 0:
        errors.append("Purchase price must be greater than zero.")
    if purchase.get("down_payment", 0) < 0 or purchase.get("down_payment", 0) > price:
        errors.append("Down payment cannot exceed the purchase price. Enter a value from Rs. 0 to the purchase price.")
    if purchase.get("annual_rate", 0) < 0:
        errors.append("Interest rate cannot be negative.")
    if int(purchase.get("tenure", 0)) <= 0:
        errors.append("Loan tenure must be a positive integer.")
    if purchase.get("alternative_price", 0) <= 0:
        errors.append("Lower-cost alternative price must be greater than zero.")
    return errors
