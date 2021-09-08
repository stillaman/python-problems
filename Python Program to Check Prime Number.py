num = int(input("Enter number:: "))
for i in range (2,num):
    if num%i == 0:
        print("The Given number is not Prime Number!!")
        break
else:
    print("The Given Number is a Prime Number!!")
    

