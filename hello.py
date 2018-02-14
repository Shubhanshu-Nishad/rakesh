print("Twinkle,Twinkle,little star,\n",
      "\t how i wonder what you are ! \n",
      "\t\t up above the world so high \n",
      "\t\t Like a diamond in the sky \n",
       " Twinkle, twinkle, little star \n",
        "\t how i wonder what you are,")


num = input("Input some comma seprated numbers : ")
values=num.split(",")
print('hy : ',values)
tuple = tuple(values)
print('tuple :',tuple)

print(values[0])
print(tuple[-1])

values.append(9)
print(values)

values[1]=5
print("Added New value to position Second", values)


'''
print(tuple[0:3])
tuple[1]=10
print("tuple after added value", tuple)'''

abs(1)
print(abs.__doc__) 