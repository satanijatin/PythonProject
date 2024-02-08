start = int(input("Enter the start range: "))
end = int(input("Enter the end range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

