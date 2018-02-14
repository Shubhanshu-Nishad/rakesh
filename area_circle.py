radius=float(input("Give a number: "))
#radius=int(radius)
area=(3.14285714286)*radius**2
print("the area is: ",area)
perimeter=2*3.14*radius
print("The perimeter is: ",perimeter)

filename=input("Give a file name with extention: ")
name=filename.split(".")
print(name[-1])