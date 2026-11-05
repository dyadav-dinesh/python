# Compute simple interest and compound interest for given principal, rate, years.

p = int(input("Enter the Principal amount:- "))
r = float(input("Enter the Annual interest rate:- "))
t = int(input("Time duration in years:- "))
n = int(input("Number of Times Interest Is Compounded:- "))

# SI = p*r*t /100
# print(f"This is the SI:- {SI}")

# CI = p*(1 + r/(100*n))**(n*t) - p  
# print(f"This is the CI:- {CI}")


print(" Enter A for for calculating the SI, B for CI and C for both.")
user_input = input("Enter your choice:- ")
SI = p*r*t /100
if n > 0:
    CI = p*(1 + r/(100*n))**(n*t) - p  
else:
    CI = "n must be greater than 0"

if user_input == "A":
    print(f"This is the SI:- {SI}")
elif user_input == "B":
    print(f"This is the CI:- {CI:.2f}:")
elif user_input == "C":
    print(f"This is the SI:- {SI}")
    print(f"This is the CI:- {CI:.2f}")
else:
    print("Invalid choice")