n = int(input ("Enter a number: - ") ) 
d = 2 
flag = False 
while d < n: 
    if (n % d == 0): 
        flag = True 
    d = d+ 1 
if flag: 
    print(str(n) + " not a prime") 
else:
    print(str(n) + " is a prime " )
