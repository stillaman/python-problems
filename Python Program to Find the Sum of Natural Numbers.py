num = int(input())

sum = 0

for i in range(num+1):
    sum+=i
print(sum)

#Or Alternatively we can do

num = int(input())
sum = (num*(num+1))/2
print(sum)
