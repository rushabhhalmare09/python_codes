
##Check why it is printing None in result after printing correct output
##Star will be printed
def pattern(num):
    i = 1
    while i <= num:
        j = 1
        while j <= num - i +1:
            print(num - i +1, end=" ")
            j = j + 1
        print()
        i = i + 1

num1= int(input("Enter a number: - "))
func_obj = pattern(num1)

print(func_obj)



## Without Function        
# num = int(input("Enter a number: -"))
# i = 1
# while i <= num:
#     j = 1
#     while j <= num:
#         print("*", end=" ")
#         j = j + 1
#     print()
#     i = i + 1