
def pattern(num):
    i = 1
    while i <= num:
        spaces = 1
        while spaces <= num - i:   ##to print spaces
            print(' ', end="")
            spaces = spaces + 1
        j = 1
        n = 1
        while j <= i:      ##to print numbers
            print(n, end="")
            j = j + 1
            n = n + 1
        #For Dec
        n = i -1
        while spaces <= num - i:   ##to print spaces
            print(' ', end="")
            spaces = spaces + 1
        j = 1
        n = 1
        while n >= 1:
            print(n, end="")
            n = n -1
        print()
        i = i + 1

num1= int(input("Enter a number: - "))
func_obj = pattern(num1)

print(func_obj)
