a = int(input("Enter the number of prime numbers you want: "))

count = 0
num = 2

while count < a:
    found = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            found = 0
            break
    if found:
        print(num)
        count += 1
    num += 1
