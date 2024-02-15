start = int(input("Enter the lower range: "))
end = int(input("Enter the upper range: "))

print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end):
    order = len(str(num))

    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
