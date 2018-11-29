import sys

sum = 0
digit_string = sys.argv[1]
if digit_string.isdigit():
    for i in digit_string:
        sum = sum + int(i)
else:
    print("Input is not number")
print(sum)
