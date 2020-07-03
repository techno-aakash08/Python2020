#Given a 32-bit signed integer, reverse digits of an integer
#Input: 123
#Output: 321

n = 123; 
rev = 0
  
while(n > 0): 
    a = n % 10
    rev = rev * 10 + a 
    n = n / 10
      
print(rev)
