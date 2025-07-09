num = int(input("Enter a number: "))
digits = []
is_unique = True
temp = num

while temp > 0:
    digit = temp % 10
    if digit in digits:
        is_unique = False
        break
    digits.append(digit)
    temp = temp // 10

if is_unique:
    print("Unique Number")
else:
    print("Not Unique Number")
