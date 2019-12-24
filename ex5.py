#variables and format string print(f"text {variables}")

my_name = 'Akhilesh Gundaboina'
my_age = 25 # not a lie
my_height = 6 # feet
height_in_cm = round(my_height*30.48)  #centimeter
my_weight = 95 # kgs
weight_in_lbs = round(my_weight*2.2)  #pounds
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} feet tall.")
print(f"or He's {height_in_cm} centimeters tall.")
print(f"He's {my_weight} kgs heavy.")
print(f"or He's {weight_in_lbs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
