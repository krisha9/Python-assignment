print('''1 To 'Add' two numbers 
2 To 'Subtract' two numbers 
3 For 'Multiplication' of  two numbers 
4 For 'Division''')

ct=1
while ct == 1:
	ch=int(input("Enter your choice: "))
	if ch>4:
		print("invalid choice")
	else:
		x=int(input("Enter your first no: "))
		y=int(input("Enter the second no: "))
		if ch == 1:
			print("The Addition of both the no.s is : ",x+y)
			
		elif ch== 2:
			print("The subtraction of  the no.s is : ",x-y)
			
		elif ch == 3:
		    	print("The multiplication of two no.s is : ",x*y)
		    
		elif ch == 4:
			print(" Dividing 1st no. by 2nd no. : ",x/y)
			
		a=input("do you wish to continue to calculate?type(yes/no)")
		if a=='yes':
			ct=1
		else:
			ct=0
		



