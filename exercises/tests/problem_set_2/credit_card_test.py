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


def test_pmt_to_pay_bal_in_year():
    balance = 3329
    interest_rate = 0.2
    assert credit_card.pmt_to_pay_bal_in_year(balance, interest_rate) == 310

    balance = 4773
    interest_rate = 0.2
    assert credit_card.pmt_to_pay_bal_in_year(balance, interest_rate) == 440

    balance = 3926
    interest_rate = 0.2
    assert credit_card.pmt_to_pay_bal_in_year(balance, interest_rate) == 360
