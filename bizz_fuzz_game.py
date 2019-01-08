# -*- coding: utf-8 -*-
# BizzFuzz game


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    i = 2
    limit = int(number ** 0.5)
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
