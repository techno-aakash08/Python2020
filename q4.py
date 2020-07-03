#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
def isPalindrome(n): 


	divisor = 121
	while (n / divisor >= 10): 
		divisor *= 10

	while (n != 0): 
		
		leading = n // divisor 
		trailing = n % 10
		

		if (leading != trailing): 
			return False

		n = (n % divisor)//10
		

		divisor = divisor/100
		
	return True


if(isPalindrome(121)): 
	print('Yes, it is palindrome') 
else: 
	print('No, not palindrome') 


