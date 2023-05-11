

def min_operations_to_make_beautiful(binary_string):
    n = len(binary_string)
    # Count the number of operations needed to make the string start with '0'
    count1 = 0
    for i in range(n):
        if i % 2 == 0 and binary_string[i] != '0':
            count1 += 1
        elif i % 2 == 1 and binary_string[i] != '1':
            count1 += 1
    # Count the number of operations needed to make the string start with '1'
    count2 = 0
    for i in range(n):
        if i % 2 == 0 and binary_string[i] != '1':
            count2 += 1
        elif i % 2 == 1 and binary_string[i] != '0':
            count2 += 1
    # Return the minimum of the two counts
    return min(count1, count2)

num1 = str(input())
num = min_operations_to_make_beautiful(num1)

print(num)

#--Meaning of a Problem Statement
# The problem statement describes a scenario where you are given a binary string STR that contains only the characters ‘0’ and ‘1’. A binary string is considered beautiful if it contains alternating '0’s and '1’s. For example, the binary strings '0101', '1010', '101', and '010' are all beautiful because they contain alternating '0’s and '1’s.

# The goal is to make the given binary string STR beautiful by performing a series of operations on it. In each operation, you can choose to convert a ‘0’ into a ‘1’ or a ‘1’ into a ‘0’. The task is to determine the minimum number of operations required to make STR beautiful.

# For example, if STR is '00110', you can make it beautiful by performing the following operations:

# Convert the second ‘0’ into a ‘1’ to get '01110'.
# Convert the third ‘1’ into a ‘0’ to get '01010'.
# After these two operations, STR is now beautiful because it contains alternating '0’s and '1’s. The minimum number of operations required to make STR beautiful is 2.

# I hope this explanation helps you understand the problem statement. Is there anything else you would like to know?

#---_EXPLANATION---

#min_operations_to_make_beautiful
# Sure! The function min_operations_to_make_beautiful takes a binary string as input and returns the minimum number of operations required to make it beautiful.

# First, the function calculates the length of the input binary string and stores it in the variable n.

# Then, the function initializes two variables count1 and count2 to 0. These variables will be used to count the number of operations needed to make the string start with ‘0’ and the number of operations needed to make the string start with ‘1’, respectively.

# Next, the function uses a for loop to iterate over the characters in the binary string. For each character, the function checks if its index is even or odd. If the index is even and the character is not ‘0’, the function increments count1 by 1. If the index is odd and the character is not ‘1’, the function also increments count1 by 1. This counts the number of operations needed to make the string start with ‘0’.

# After the first for loop, the function uses another for loop to do the same thing, but this time it counts the number of operations needed to make the string start with ‘1’. If the index is even and the character is not ‘1’, the function increments count2 by 1. If the index is odd and the character is not ‘0’, the function also increments count2 by 1.

# Finally, the function returns the minimum of count1 and count2. This is the minimum number of operations required to make the binary string beautiful.

# I hope this explanation helps you understand how the function works. Is there anything else you would like to know?

# Sure! Here is an example of how to use the min_operations_to_make_beautiful function:

# binary_string = '00110'
# result = min_operations_to_make_beautiful(binary_string)
# print(f"The minimum number of operations required to make the binary string '{binary_string}' beautiful is {result}.")
# In this example, we define a binary string binary_string with the value '00110'. Then, we call the min_operations_to_make_beautiful function with binary_string as the argument and store the result in the variable result. Finally, we print the result using a formatted string.

# When you run this code, it will output the following:

# The minimum number of operations required to make the binary string '00110' beautiful is 2.
# This means that it takes a minimum of 2 operations to make the binary string '00110' beautiful. You can change the value of binary_string to test the function with different inputs.

# I hope this example helps you understand how to use the min_operations_to_make_beautiful function. Is there anything else you would like to know?


# No, the input to the min_operations_to_make_beautiful function must be a binary string, which means it can only contain the characters ‘0’ and ‘1’. If you pass a string that contains characters other than ‘0’ and ‘1’ to the function, it will not work correctly.

# For example, if you call the function with the input 'STRING', it will not return a meaningful result because the input is not a binary string.

# It is important to make sure that the input to the function is a valid binary string before calling the function. Is there anything else you would like to know?