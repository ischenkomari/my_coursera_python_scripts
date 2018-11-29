import random
import statistics

numbers = []
number_size = random.randint(10, 15)

for _ in range(number_size):
    numbers.append(random.randint(10, 20))

print(numbers)

numbers.sort()

half_size = len(numbers) // 2
median = None

if number_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1: half_size +1]) /2

print(median)
print(numbers)
print(statistics.median(numbers))
