#Declaring variables with different data types
a= 10 #integer
b= "20" #string

#printing values before swapping
print("Before swapping:")
print("a =",a,"b=",b)

#Type casting and swapping
a, b=int(b), str(a) #converting 'b' to integer and 'a' to string

#printing vales after swapping
print("after swapping:")
print("a =", a, "b =", b)