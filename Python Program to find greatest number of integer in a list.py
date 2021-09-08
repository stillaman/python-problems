a = []
x = int(input("Enter number of terms:: "))
for i in range (0,x):
    a.append(input())
a.sort()
print(int(a[x-1]))
