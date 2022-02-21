# 6.5 track your investments

# P(1 + r/100n)^nt

# P = principle amt
# r = interest rate w/o % per annum
# t = no. of years
# n = no. of times in a year compounding occurs

# amount ( 1 + rate) ** years

def invest(amount, rate, years):
	amount = float(amount)
	rate = float(rate)
	years = int(years)
	for t in range(years):
		t += 1
		final = amount * ((1 + rate)**t)
		print(f"year {t}: ${final:.2f}")

# invest(100, .05, 4)

amount = input("what's the initial amount: ")
rate = input("what's the annual percentage rate: ")
years = input("what's the number of years: ")

invest(amount, rate, years)
