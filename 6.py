# Read a number of seconds and print it as HH:MM:SS.
total = int(input("Enter the seconds:- "))

HH = total // 3600
MM = (total % 3600) // 60
SS = total % 60

print(f"{HH:02}:{MM:02}:{SS:02}")