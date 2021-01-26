#leap years
print("Enter a year.")
years = input()
if int(years)%400 == 0:
    print("This is a leap year.")
elif int(years)%100 == 0:
    print("This is not a leap year.")
elif int(years)%4 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")