year = int(input("Enter year:: "))
if year%400==0:
        leap = True
elif year%100==0:
        leap = False
elif year%4==0:
        leap = True
else:
    pass
if leap == True:
    print("Leap year!!")
else:
    print("Not a Leap Year!!")

#or Alternatively

year = int(input("Enter an year "))
if year%4==0 or year%400==0:
    if year%100==0:
        print("not leap!!")
    else:
        print("Leap!!")
else:
    print("not leap")
    