#bmi calculator with different choices
print("Enter 1 to find bmi through weight in pound and height in Meter")
print("Enter 2 to find bmi through weight in kg and height in cm")
choice=int(input("choice:"))
weight = None
height = None
bmi = None
if (choice==1):
 weight = float(input("Enter weight in pounds:"))
 height = float(input("Enter height in meters:"))
 bmi = weight*0.45359237/height**2
 print ("your Bmi is :",bmi)
 
elif (choice==2): 
 weight = float(input("Enter weight in kg:"))
 height = float(input("Enter height in cm:"))
 bmi= weight/((height/100)**2)
 print ("your Bmi is :",bmi)
else:
    print("incorrect choice")



