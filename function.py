def printNumber():
    print("My name is rakesh")

def printAdress():
    print("My adress is basundhara ")



printAdress()
printNumber()



def sum(x,y):
    z=x+y
    print(z)

sum(5,6)
sum(120,10)

def sub(a,b):
    print(a-b)

sub(100,50)

def string(b,c):
    print(b+c)

string("Rakesh","raut")


def sumReturn(x,y):
    z=x+y
    return z

sum=sumReturn(10,40)

print(sum)






def area(radius):
    a=22/7*radius**2
    return a

area=area(10)
print(area)


def person(name="Rakesh", lname="Raut"):
    print("Name is: ", name, " and Last name is: ", lname)

person("Hari", "Rai")



def marks(name, *marks):
    print(name)
    print(marks)

marks("Rakesh", 44, 56, 33, 4 ,5)



# to find the max value between two numbers
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

equal=max_of_two(4,8)


print("The maximum of two number is: ", equal)



# to find the greatest number between three numbers
def two( x, y ):
    if x > y:
        return x
    return y
def three( x, y, z ):
    return two(x,two( y, z ) )
print("The gratest number is: ", three(3, 6, 8))

# to print the sum of the three number
def sum_of_three(a, b, c):

    sum = a + b + c
    if a == b == c:

        sum= sum * 3
    return sum

print(sum_of_three(1, 2, 3))
print(sum_of_three(3, 3, 3))