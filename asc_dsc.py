#Question: write a program to print the letter in ascending and descending order.

#Solution is  given below:

#Program to print the letters in ascending order.
list = ["f", "a", "u", "z", "g", "l", "b", "x", "s"]
list.sort()
print("This is sorted in ascending order: ", list)

#Program to print the letters in descending order.
list.sort(reverse=True)

print("This is sorted in descending order: ",list)