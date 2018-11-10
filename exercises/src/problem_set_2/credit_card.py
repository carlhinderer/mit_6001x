
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


def fast_pmt_to_pay_bal_in_year(balance, annual_int_rate):
    monthly_int_rate = annual_int_rate / 12
    lower_bound = balance / 12
    max_yearly_rate = (1 + monthly_int_rate)**12
    upper_bound = (balance * max_yearly_rate) / 12
    while True:
        running_balance = balance
        guess = (lower_bound + upper_bound) / 2
        for month in range(12):
            running_balance -= guess
            running_balance *= (1 + monthly_int_rate)
        if round(running_balance, 2) == 0:
            break
        elif running_balance > 0:
            lower_bound = guess
        else:
            upper_bound = guess
    return round(guess, 2)
