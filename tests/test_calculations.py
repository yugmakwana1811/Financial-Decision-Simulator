import pytest
from modules.calculations import *

def test_surplus_and_deficit():
    assert monthly_surplus(50000,25000,8000,2000)==15000
    assert monthly_surplus(100,80,30)==-10
def test_coverage_zero_and_regular(): assert emergency_coverage(150000,25000)==6 and emergency_coverage(10,0) is None
def test_interest_formulas():
    assert simple_interest(1000,10,2)==200
    assert compound_amount(1000,10,2)==pytest.approx(1210)
def test_emi_zero_interest(): assert emi(12000,0,12)==1000
def test_emi_positive_interest(): assert emi(100000,12,12)==pytest.approx(8884.88,abs=.1)
def test_emi_edges():
    assert emi(0,12,12)==0
    with pytest.raises(ValueError): emi(1,-1,12)
    with pytest.raises(ValueError): emi(1,1,0)
def test_repayment_future_value_goal_delay():
    assert total_repayment(1000,12)==12000
    assert future_value(1000,10,2)==pytest.approx(1210)
    assert goal_delay(10000,5000)==2 and goal_delay(1,0) is None
