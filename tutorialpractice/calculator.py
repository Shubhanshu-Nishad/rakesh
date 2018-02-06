a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print("which operation you want to do:- ")
user_input=input("press a for addition,s for subtraction,d for division and m for multiplication: ")

if user_input == "a":
	print(a+b)
elif user_input=="s":
	print(a-b)
elif user_input=="d":
	print(a/b)
elif user_input=="m":
	print(a*b)
else:
	print("You typed other character")



#,"press s for subtraction","press d for division","press m for multiplication")