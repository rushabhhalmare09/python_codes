
##Check why it is printing None in result after printing correct output
##Number will be printed instead of *



def pattern(num, row, column):
    i = row
    while i <= num:
        j = column
        while j <= num:
            print(num - j + 1, end=" ")
            j = j + 1
        print()
        i = i + 1

num1= int(input("Enter a number: - "))
row= int(input("Enter a row number: - "))
column= int(input("Enter a column number: - "))

# row and column put it 1 only 
func_obj = pattern(num1,row, column)

print(func_obj)




#   =========or=============


# def pattern(num, row, column):
#     i = row
#     while i <= num:
#         j = column
#         n = num
#         while j <= num:
#             print(n, end=" ")
#             j = j + 1
#             n = n - 1
#         print()
#         i = i + 1

# num1= int(input("Enter a number: - "))
# row= int(input("Enter a row number: - "))
# column= int(input("Enter a column number: - "))

# # row and column put it 1 only 
# func_obj = pattern(num1,row, column)

# print(func_obj)




## Without Function        
# num = int(input("Enter a number: -"))
# # i = 1
#     while i <= num:
#         j = column
#         while j <= num:
#             print(num - j + 1, end=" ")
#             j = j + 1
#         print()
#         i = i + 1