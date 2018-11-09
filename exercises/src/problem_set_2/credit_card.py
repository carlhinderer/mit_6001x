
def bal_after_years_min_pmts(balance, annual_int_rate, monthly_pmt_rate):
    monthly_int_rate = annual_int_rate / 12
    for month in range(12):
        min_pmt = balance * monthly_pmt_rate
        balance -= min_pmt
        balance *= (1 + monthly_int_rate)
    return round(balance, 2)


def pmt_to_pay_bal_in_year(balance, annual_int_rate):
    monthly_int_rate = annual_int_rate / 12
    payment = 0
    running_balance = balance
    while running_balance > 0:
        running_balance = balance
        payment += 10
        for month in range(12):
            running_balance -= payment
            running_balance *= (1 + monthly_int_rate)
    return payment
