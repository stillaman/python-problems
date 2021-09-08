x = int(input())
y = int(input())
z = int(input())

if x>y:
    if x>z:
        print(x, "is Greatest of three")
elif y>x:
    if y>z:
        print(y, "is Greatest of three")
else:
    print(Z," is greatest of three")

#Or Alternatively

x = int(input())
y = int(input())
z = int(input())
if x>y and x>z:
    print(x,"is greatest")
elif y>x and y>z:
    print(y, "is greatest")
else:
    print(z, "is greatest")
    