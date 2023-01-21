def factorial():
	f=int(input("enter factorial number"))
	fact=f
	k=1
	while f>0:
		e=f
		k=k*e
		f-=1
	print(f"The factorial [ {fact}! ] =", k)
factorial()

#factorial !