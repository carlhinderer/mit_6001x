import pytest
from src.problem_set_2 import credit_card


def test_bal_after_years_min_pmts():
    balance = 42
    interest_rate = 0.2
    pmt_rate = 0.04
    assert credit_card.bal_after_years_min_pmts(balance, interest_rate, pmt_rate) == 31.38

    balance = 484
    interest_rate = 0.2
    pmt_rate = 0.04
    assert credit_card.bal_after_years_min_pmts(balance, interest_rate, pmt_rate) == 361.61
