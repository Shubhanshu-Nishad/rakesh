num=input("Enter a Number: ")
num=int(num)
if num%2==0:
    print("The Given Number is Even")
else:
    print("The Given Number is Odd")


Nepali=["Dhido","Gundruk","Daal"]
indian=["Paratha","Naan","Samosa"]
italian=["Pizza","Pasta","Risotto"]

dish=input("Enter a Dish name: ")
if dish in Nepali:
    print("This is Nepali Dish")
elif dish in indian:
    print("This is Indian Dish")
elif dish in italian:
    print("This is italian Dish")
else:
    print("Sorry! i don't know the name of dish you entered")