from modules.consequence_engine import build_scenarios, baseline

PROFILE={"primary_income":50000,"other_income":0,"essential":25000,"non_essential":8000,"existing_debt":2000,"savings":150000,"goal_contribution":5000}
PURCHASE={"price":60000,"down_payment":10000,"annual_rate":12,"tenure":12,"alternative_price":45000,"delay_months":6,"monthly_wait_saving":8000,"wait_price_change":0,"growth_rate":6,"opportunity_years":3}
def test_baseline(): assert baseline(PROFILE)["surplus"]==15000
def test_four_scenarios(): assert len(build_scenarios(PROFILE,PURCHASE))==4
def test_cash_and_alternative():
    cash,_,_,alt=build_scenarios(PROFILE,PURCHASE)
    assert cash.total_cost==60000 and cash.savings_remaining==90000
    assert alt.total_cost==45000 and alt.savings_remaining==105000
def test_emi_and_wait():
    _,loan,wait,_=build_scenarios(PROFILE,PURCHASE)
    assert loan.interest_paid>0 and loan.monthly_surplus<15000
    assert wait.savings_remaining==138000
def test_full_down_payment():
    p=dict(PURCHASE,down_payment=60000)
    assert build_scenarios(PROFILE,p)[1].monthly_emi==0
