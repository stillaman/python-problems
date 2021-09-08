num = int(input())
f1 = 0
f2 = 1
sum = 0
if num <=0:
    print("invalid")
elif num==0:
    print(f1)

for i in range (0,num):
    print(f1)
    term = f1+f2
    f1 = f2
    f2 = term
    i+=1

#Or Alternativelt we can do

num = int(input())
f1 = 0
f2 = 1
i = 0
if num <=0:
    print("invalid")
elif num==0:
    print(f1)
else:
    while i<num:
        print(f1)
        term = f1+f2
        f1 = f2
        f2 = term
        i+=1
        