from modules.consequence_engine import build_scenarios
from modules.stress_engine import apply_stress, PRESETS
from tests.test_consequence_engine import PROFILE, PURCHASE

def test_income_stress_reduces_surplus():
    r=build_scenarios(PROFILE,PURCHASE)[1]
    assert apply_stress(PROFILE,r,PRESETS["Income decreases by 25%"])['surplus'] < r.monthly_surplus
def test_emergency_expense_reduces_savings():
    r=build_scenarios(PROFILE,PURCHASE)[0]
    assert apply_stress(PROFILE,r,PRESETS["Unexpected expense of Rs. 50,000"])['savings']==r.savings_remaining-50000
def test_combined_shock():
    r=build_scenarios(PROFILE,PURCHASE)[1]; s=apply_stress(PROFILE,r,PRESETS["Combined: 20% income fall + Rs. 25,000 expense"])
    assert s['savings']==r.savings_remaining-25000 and s['surplus']<r.monthly_surplus
