
def bal_after_years_min_pmts(balance, annual_int_rate, monthly_pmt_rate):
    monthly_int_rate = annual_int_rate / 12
    for month in range(12):
        min_pmt = balance * monthly_pmt_rate
        balance -= min_pmt
        balance *= (1 + monthly_int_rate)
    return round(balance, 2)
