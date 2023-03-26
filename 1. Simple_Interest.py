principal = int(input("Enter principal amount: - "))
rate = int(input("Enter rate of interest: - "))
time = int(input("Enter Time Period: - "))

SimpleInterest = principal * rate * time / 100

print("The simple Interest is: - " + str(SimpleInterest))
