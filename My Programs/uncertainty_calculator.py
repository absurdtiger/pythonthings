# Program for calculating percentage uncertainties.

number = float(input("Enter a value: "))
uncertainty = float(input("Enter an uncertainty: "))
percentage = (uncertainty/number)
print(f"Percentage Uncertainty is {percentage:.2%}")
