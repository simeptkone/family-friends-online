import sys
from collections import Counter

a = "Ganesh Ramkumar Babu MSK"
b = len(a)
print(a,b)
c = a.split()
print(c, len(c))

count = Counter(a.upper())
print(count)
print(count['a'])  # Output: 4

print(sys.version)

