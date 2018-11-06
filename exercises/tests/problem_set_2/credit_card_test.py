import pytest
from src.problem_set_2 import credit_card


def test_make_years_minimum_payments():
    balance = 42
    interest_rate = 0.2
    pmt_rate = 0.04
    assert credit_card.make_years_minimum_payments(balance, interest_rate, pmt_rate) == 'test'