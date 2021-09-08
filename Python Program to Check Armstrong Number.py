a = input()
b = len(a)
sum = int(a)
temp = 0
for i in a:
    
    temp = temp+int(i)**b
if temp == sum:
    print("It is an Armstrong number!!")
else:
    print("It is not an Armstrong number!!")