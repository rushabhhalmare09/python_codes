num1 = int(input("Enter a number: - "))
count = 1
sum = 0

while count <= num1:
    if (count % 2 == 0):
        sum = sum + count
        count += 1
    else:
        count += 1
print(sum)
