import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b*b-4*a*c

print(d)

if d>0:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print(x1, x2)
else: print("Complex")
