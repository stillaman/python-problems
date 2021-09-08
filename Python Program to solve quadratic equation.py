import cmath
a = float(input("Enter coefficient of x² :: "))
b = float(input("Enter coefficient of x :: "))
c = float(input("Enter constant term :: "))
d = (b**2) - (4*a*c)
sol1, sol2 = (-b+cmath.sqrt(d))/2*a, (-b-cmath.sqrt(d))/2*a
print("Solution of the given quadratic equation is :: {0} and {1}" .format(sol1,sol2))