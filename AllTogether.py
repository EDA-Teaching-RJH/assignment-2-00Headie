import random
numbers = [random.randint(1,100) for _ in range(10)]
print("Original list:", numbers)

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
    else:
        i += 1
print("List of odd numbers:", numbers)
