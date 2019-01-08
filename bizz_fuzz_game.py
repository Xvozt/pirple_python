# -*- coding: utf-8 -*-
# BizzFuzz game

# Function that returns if number is prime or not


def is_prime(number):
    # 1 is not Prime and 2 is Prime
    if number == 1:
        return False
    if number == 2:
        return True
    i = 2
    limit = int(number ** 0.5)  # no need to go through all dividers
    while i <= limit:
        if number % i == 0:
            return False
        i += 1
    return True


for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif is_prime(i) is True:
        print("Prime")
    else:
        print(i)
