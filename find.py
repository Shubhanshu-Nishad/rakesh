import random
age = []
for i in range(100):
    random_age=random.randint(16,50)
    age.append(random_age)

print("The list of ages: ",age)
print("The total number of sample age: ", len(age))
print("The maximum age is: ", max(age))
print('The minimum age is: ', min(age))

your_age=int(input("Enter your age to find your matching person num but ur age must be less than 50 n greater than 15: "))
print("Matching person number is: ",age.count(your_age))


