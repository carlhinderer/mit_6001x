from . import credit_card


def test_bal_after_years_min_pmts_interactively():
    balance = float(input('Enter the starting balance: '))
    annual_int_rate = float(input('Enter the annual interest rate: '))
    monthly_pmt_rate = float(input('Enter the monthly_pmt_rate: '))
    remaining_bal = credit_card.bal_after_years_min_pmts(balance, annual_int_rate, monthly_pmt_rate)
    print('Remaining balance:', remaining_bal)
