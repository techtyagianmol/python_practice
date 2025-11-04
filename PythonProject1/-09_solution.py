year = int(input("Enter year:-"))

if (year%400 == 0) or (year%4 == 0 and year % 100 !=0):
    print(str(year)+" "  + "is leap year")
else:
    print(str(year) +" " + "is not leap year")