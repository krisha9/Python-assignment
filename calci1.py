print(" 1 To 'Add' two numbers ")
print(" 2 To 'Subtract' two numbers ")
print(" 3 To 'Multiplication' two numbers ")
print(" 4 For 'Division' ")

choice=int(input("Enter your choice.: "))
x=int(input("Enter your first no.: "))
y=int(input("Enter the second no.: "))
while (choice<5):
	if choice == 1:
		print("The 'Addition' of both the no.s is : ",x+y)
		break
	elif choice== 2:
		print("The 'subtraction' of  the no.s is : ",x-y)
		break
	elif choice == 3:
		print("The multiplication of two no.s is : ",x*y)
		break
	elif choice == 4:
		print("'Dividing' 1st no. by 2nd no. : ",x/y)
		break
	else:
		print("Invalid coice")
		
	
