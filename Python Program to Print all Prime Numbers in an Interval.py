ll = int(input("Enter lower limit:: "))
ul = int(input("Enter Upper limit:: "))

for num in range (ll, ul+1):
    for i in range (2, num): 
        if num%i == 0:
            break
    else:
        print(num)