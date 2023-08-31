n = int(input("Enter a 3 digit number: "))
a = n // 100
b = n % 100 // 10
c = n % 10

if a - c == 0 or b - c == 0:
    print("Factorial of middle digit: ", factorial(b))
else:
    print("Middle digit number of tribonacci series: ", tribonacci(b))

def factorial(n):
    if n == 0:
        return 1
    return n  factorial(n - 1)
    
    def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
