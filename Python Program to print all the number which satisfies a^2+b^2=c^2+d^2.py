# a^2+b^2=c^2+d^2
for a in range (100):
    for b in range (100):
        for c in range(100):
            for d in range (100):
                if a and b!=d or c:
                    if a**2+b**2-c**2-d**2==0:
                        print(a, b, c, d)
                    else:
                        break