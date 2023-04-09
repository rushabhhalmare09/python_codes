N = int(input("Enter a number: - "))

even = 0
odd = 0
while(N > 0):
    rem = N % 10
    N = N // 10
    if (rem % 2 == 0):
        even = even + rem
    else:
        odd = odd + rem
print(" Sum of Even number : - ", even, "Sum of Odd number : - ", odd)
