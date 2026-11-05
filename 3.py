# Convert Celsius to Fahrenheit and back.
Celsius_temp = float(input("Enter tempreature in celsius:- "))


fahrenheit_temp = (Celsius_temp * 1.8) + 32
print(f"Temp in Fahrenheit {fahrenheit_temp }°F")

print("press a to covert Fahrenheit to Celsius \n For different value press b")
# user_input = input("press a to covert Fahrenheit to Celsius anf For different value press b:- ")

# if user_input == "a":
#     celsius_temp = (fhrenheit_temp - 32) / 1.8
#     print(f"Temp in Celsius_temp {celsius_temp} ")
# else:
#     fahrenheit_temp = float(input("Enter tempreature in Fahrenheit:- "))
#     celsius_temp = (fahrenheit_temp - 32) / 1.8
#     print(f"Temp in Celsius_temp {celsius_temp} ")
    
user_input = input("Press a to convert back to Celsius, or b to enter a new Fahrenheit value: ").strip().lower()

if user_input == "a":
    celsius_temp = (fahrenheit_temp - 32) / 1.8
    print(f"Temp in Celsius: {celsius_temp:.2f}°C")
elif user_input == "b":
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp = (fahrenheit_temp - 32) / 1.8
    print(f"Temp in Celsius: {celsius_temp:.2f}°C")
else:
    print("Invalid choice")
