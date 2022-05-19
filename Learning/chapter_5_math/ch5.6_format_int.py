### 5.6 Print numbers in style ###

# in formatted strings, use {:.2f to round to 2 decimal places as a fixed-point number
# you can present percentage with {:.2%}
# present currency easier with {:,.2f}

# ex1
result1 = 3 ** .125
print(f"{result1:.3f}")

# ex2
result2 = 150000
print(f"${result2:,.2f}")

# ex3
result3 = 2/10
print(f"{result3:.0%}")


