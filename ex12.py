#Prompting People to calculate BMI index

age = input("enter you age:")
height = float(input("enter your height in cms:"))
weight = float(input("enter your weight in kgs:"))

print(f"So you are {age} years old, {height} ft tall and {weight} kgs heavy")
isValid = input("Is the above information correct? 'y/n'?")
if (isValid == 'y'):
   BMI = (weight/((height/100)**2))
   print(f"BMI = {BMI}")
else:
   print("enter correct details")
   exit()

if (BMI > 40):
    print("Extreme Obesity(class 3)")
elif(BMI < 39.9 and BMI > 35):
    print("Obesity(class 2)")
elif (BMI <34.9 and BMI > 30):
    print("Obesity(class 1)")
elif (BMI <29.9 and BMI > 25):
    print("Overweight")
elif (BMI <24.9 and BMI > 18.5):
    print("Normal Weight")
elif (BMI <18.5):
    print("Underweight")
