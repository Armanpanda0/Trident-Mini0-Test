def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

number = int(input("Enter a 3-digit number: "))
if len(str(number)) != 3:
    print("Please enter a valid 3-digit number.")
else:
    first_digit = number // 100
    middle_digit = (number // 10) % 10
    last_digit = number % 10

    difference = abs(first_digit - last_digit)
    
    if difference % 2 == 0:
        result = factorial(middle_digit)
        print(f"Factorial of middle digit ({middle_digit}) is: {result}")
    else:
        result = tribonacci(middle_digit)
        print(f"Middle digit of tribonacci series ({middle_digit}th term) is: {result}")
