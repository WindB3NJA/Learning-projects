x = 1213

reverse = 0
while x > 0:
    last_digit = x % 10
    reverse = reverse * 10 + last_digit
    x = x // 10

print("Final: " + str(reverse))
