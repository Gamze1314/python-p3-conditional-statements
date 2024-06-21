#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    return "Access granted" if (username == "admin" or username == "ADMIN") and password == "12345" else "Access denied"


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 < temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:  # Check if the number is divisible by both 3 and 5
        return "FizzBuzz"
    elif num % 3 == 0:  # Check if the number is divisible by 3
        return "Fizz"
    elif num % 5 == 0:  # Check if the number is divisible by 5
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        operations = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2
        }
        result = operations.get(operation)
        if result is None:
            print("Invalid operation!")
        return result
    except ValueError:
        return "Invalid value"

    # try/except for exception/error handling

