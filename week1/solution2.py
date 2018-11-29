import sys

try:
    num_steps = int(sys.argv[1])
except Exception as e:
    print("PLEASE PASS THE DIGITS")
    exit()

for i in range(num_steps):
    print(" "*(num_steps-i-1)+"#"*(i+1))
