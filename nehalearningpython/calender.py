import calendar

def calce():
    print(calendar.weekheader(2)) #print all the weekdays in row , 2 is used for how much words u want to print
    print()

    print(calendar.firstweekday()) #to check wheather there is monday or any week and it starts with 0 'monday'
    print()

    print(calendar.month(2019,3)) #only printing the month of that year
    print()
    print(calendar.calendar(2019))
    print()


    print("#########if we want to know the day name of any year ########")
    day = print(calendar.weekday(2019,1,31))
    print(day)



    is_leap=print(calendar.isleap(2020))
    print(is_leap)
    print()
calce()


day =print(calendar.weekday(1991,7,23))
print(day)
print()

leapdays = print(calendar.leapdays(2000,2020))
print(leapdays,"printing the leapdays between 2001,2005" ,leapdays)