#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = abs(number) % 10 * (-1 if number < 0 else 1)

print(f"Last digit of {number} is {lastdigit}", end=" ")

if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is 0")
else:
    print(f"and is less than 6 and not 0")
