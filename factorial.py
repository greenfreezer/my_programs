def factorial():
	f=int(input("enter factorial number"))
	fact=f
	multiplier=1
	while f>0:
		value=f
		multiplier=multiplier*value
		f-=1
	print(f"The factorial [ {fact}! ] =", multiplier)
factorial()

#factorial !
