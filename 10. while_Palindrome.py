def checkPalindrome(num):
    temp = num
    rev = 0
    while(num> 0):
        remainder = num % 10
        rev = (rev * 10) + remainder
        num = num // 10
    
    if(temp == rev):
        return True
    else:
        return False


num = int(input("Enter a number: - "))
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')
