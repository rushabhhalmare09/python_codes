
while(1):
    a = int(input("Operation - Enter number : - "))
    
    if(a ==1 ):
        x = int(input("Enter first number: - "))
        y = int(input("Enter second number: - "))
        sum = x + y
        print(sum)
    elif(a == 2):
        x = int(input("Enter first number: - "))
        y = int(input("Enter second number: - "))
        subtract = x - y
        print(subtract)
    elif(a == 3):
        x = int(input("Enter first number: - "))
        y = int(input("Enter second number: - "))
        multiply = x * y
        print(multiply)
    elif(a == 4):
        x = int(input("Enter first number: - "))
        y = int(input("Enter second number: - "))
        division = x / y
        print(division)
    elif(a == 5):
        x = int(input("Enter first number: - "))
        y = int(input("Enter second number: - "))
        modulus = x % y
        print(modulus)
    elif(a==6):
        break
    else:
        print("Invalid Operation")