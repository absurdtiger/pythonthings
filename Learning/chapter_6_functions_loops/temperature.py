# for 6.3 converting temperatures

def convert_cel_to_far(a):
    C = float(a)
    F = C * 9/5 + 32
    return F


def convert_far_to_cel(a):
    F = float(a)
    C = (F - 32) * 5/9
    return C


prompt1 = input("Enter a temperature in degrees F: ")
output1 = convert_far_to_cel(prompt1)
print(f"{prompt1} degrees F = {output1:.2f} degrees C")

prompt2 = input("Enter a temperature in degrees C: ")
output2 = convert_cel_to_far(prompt2)
print(f"{prompt2} degrees C = {output2:.2f} degrees F")

