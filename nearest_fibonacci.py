def nearest_and_next_fibonacci(n):
    if n < 0:
        return 0, 1 
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return a, b
number = int(input())
nearest_fib, next_fib = nearest_and_next_fibonacci(number)
if number-nearest_fib==next_fib-number:
    print(f"{nearest_fib} {next_fib}")
else:
    print(f"{nearest_fib}")
