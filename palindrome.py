def palindrome():
	x=int(input("Enter the number"))
	original_integer=x
	reverse_integer=0
	while x>0:
	 reminder=x%10
	 reverse_integer= (reverse_integer*10)+reminder
	 x//=10
	if original_integer==reverse_integer:
	 print("it is palindrome",original_integer)
	else:
	 print("it is not palindrome",original_integer)
palindrome()

# palindrome is if 565 ,4334, 222, 2 and 34, 345, is not palinrome , reversing number also same is palindrome