# Swap two variables without a third variable.

num1 = int(input("Enter the num1:- "))
num2 = int(input("Enter the num2:- "))
print(id(num1), id(num2))


num1, num2 = num2, num1
print(f"{num1}, {num2}")

print(id(num1), id(num2))

