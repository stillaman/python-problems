import random
divisor = int(input())
num = []
print("Numbers which are disible by ",divisor, " are :: ")
for i in range (100):
    a = (random.randint(0,100))
    if a%divisor==0:
        print(a)
    

