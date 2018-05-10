import math
# Task 1 ----------
a = 10
b = 20
c = 30
result = a + b*(c / 2)
print("Результат при a=%d, b=%d, c=%d равен %.2f" %(a,b,c,result))

# Task 2 ----------
result = (a**2 + b**2) % 2
print("Результат при a=%d, b=%d равен %d" %(a,b,result))

# Task 3 ---------
result = (a + b)/12 * c % 4 + b
print("Результат при a=%d, b=%d, c=%d равен %.2f" %(a,b, c, result))

# Task 4 ----------
result = (a - b * c)/( a + b ) % c
print("Результат при a=%d, b=%d, c=%d равен %.2f" %(a,b, c, result))

# Task 5 ------------
result = math.fabs(a - b) /(a + b)**3 - math.cos( c )
print("Результат при a=%d, b=%d, c=%d равен %.2f" %(a,b,c,result))

# Task 6 -------------
result = (math.log10(1 + c) / -b )**4 + math.fabs(a)
print("Результат при a=%d, b=%d, c=%d равен %.2f" %(a,b,c,result))