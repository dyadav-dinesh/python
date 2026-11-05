# Read two numbers from input and print their sum, difference, product and quotient.
Num1 = int(input("First Number: "))
Num2 = int(input("Second Number: "))

print(f"Sum: {Num1 + Num2}")
print(f"Difference: {Num1 - Num2}")
print(f"Product: {Num1 * Num2}")
if Num2 != 0:
    print(f"Quotient: {Num1 / Num2}")
else:
    print("Cannot divide by zero")

