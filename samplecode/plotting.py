from matplotlib import pyplot

principal = 10000
interest_rate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal * interest_rate

pyplot.figure(1)
pyplot.plot(values)
pyplot.show()
