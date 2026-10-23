# ==============================================================================
# BASIC PYTHON PROGRAMS (1 to 10)
# ==============================================================================

# 1. Print "Hello, World!"
print("--- Program 1: Hello World ---")
print("Hello, World!")
print()

# 2. Add two numbers
print("--- Program 2: Add Two Numbers ---")
num1 = 5
num2 = 7
sum_result = num1 + num2
print(f"Sum of {num1} and {num2} is: {sum_result}")
print()

# 3. Find the largest of three numbers
print("--- Program 3: Largest of Three Numbers ---")
a, b, c = 10, 25, 15
largest = max(a, b, c)
print(f"The largest of {a}, {b}, and {c} is: {largest}")
print()

# 4. Check whether a number is even or odd
print("--- Program 4: Even or Odd Checker ---")
check_num = 14
if check_num % 2 == 0:
    print(f"{check_num} is Even")
else:
    print(f"{check_num} is Odd")
print()

# 5. Check whether a number is positive, negative, or zero
print("--- Program 5: Positive, Negative, or Zero Checker ---")
test_num = -8
if test_num > 0:
    print(f"{test_num} is Positive")
elif test_num < 0:
    print(f"{test_num} is Negative")
else:
    print(f"{test_num} is Zero")
print()

# 6. Find the factorial of a number
print("--- Program 6: Factorial of a Number ---")
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is: {fact}")
print()

# 7. Generate the Fibonacci series
print("--- Program 7: Fibonacci Series ---")
terms = 8
fib_series = [0, 1]
while len(fib_series) < terms:
    fib_series.append(fib_series[-1] + fib_series[-2])
print(f"First {terms} terms of Fibonacci series: {fib_series[:terms]}")
print()

# 8. Check whether a number is prime
print("--- Program 8: Prime Number Checker ---")
prime_check = 17
is_prime = True
if prime_check < 2:
    is_prime = False
for i in range(2, int(prime_check**0.5) + 1):
    if prime_check % i == 0:
        is_prime = False
        break
print(f"Is {prime_check} a prime number? {is_prime}")
print()

# 9. Reverse a number
print("--- Program 9: Reverse a Number ---")
original_num = 12345
reversed_num = int(str(original_num)[::-1])
print(f"Original number: {original_num}, Reversed number: {reversed_num}")
print()

# 10. Check whether a number is a palindrome
print("--- Program 10: Number Palindrome Checker ---")
pal_num = 121
is_palindrome = str(pal_num) == str(pal_num)[::-1]
print(f"Is {pal_num} a palindrome? {is_palindrome}")
print()