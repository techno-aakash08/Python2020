#Implement pow(x, n), which calculates x raised to the power n (xn).
def power(x, y): 
  
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (power(x, int(y / 2)) *
               power(x, int(y / 2))) 
    else: 
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2))) 
  
# Driver Code 
x = 2.00000; y = 10
print(power(x, y))
