# Read a number of seconds and print it as HH:MM:SS.
SS = int(input("Enter the seconds:- "))

MM = SS % 60
HH = MM % 60

print(f"{HH}:{MM}:{SS}")