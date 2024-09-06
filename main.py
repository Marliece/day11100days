print("How many seconds are in a year?")
print()
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60
secondsPerDay = secondsPerHour * 24

leapYear = input("Is it a leap year? ")
if leapYear == "yes" or leapYear == "Yes":
  secondsPerYear = secondsPerDay * 366
  print("There are", secondsPerYear, "seconds in a leap year.")
else:
  secondsPerYear = secondsPerDay * 365
  print("There are", secondsPerYear, "seconds in a year.")