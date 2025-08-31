#adding string
first_name = input("Enter First Nmae :")
last_name = input("Enter Last Name :")
space=" "
full_name = first_name+space+last_name
print("Full Name :",full_name)
print(type(full_name))

#sumof two numbers
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
sum=a+b
print("Sum of a and b",sum)

#Bmi calculator 
weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in cm:"))
bmi=weight/((height/100)**2)
print ("your Bmi is :",bmi)