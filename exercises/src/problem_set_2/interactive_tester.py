from . import credit_card


def test_bal_after_years_min_pmts():
    balance = float(input('Enter the starting balance: '))
    annual_int_rate = float(input('Enter the annual interest rate: '))
    monthly_pmt_rate = float(input('Enter the monthly_pmt_rate: '))
    remaining_bal = credit_card.bal_after_years_min_pmts(balance, annual_int_rate, monthly_pmt_rate)
    print('Remaining balance:', remaining_bal)


def test_pmt_to_pay_bal_in_year():
    balance = float(input('Enter the starting balance: '))
    annual_int_rate = float(input('Enter the annual interest rate: '))
    minimum_pmt = credit_card.pmt_to_pay_bal_in_year(balance, annual_int_rate)
    print('Lowest payment:', minimum_pmt)


def test_fast_pmt_to_pay_bal_in_year():
    balance = float(input('Enter the starting balance: '))
    annual_int_rate = float(input('Enter the annual interest rate: '))
    minimum_pmt = credit_card.fast_pmt_to_pay_bal_in_year(balance, annual_int_rate)
    print('Lowest payment:', minimum_pmt)
