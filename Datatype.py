# Datatypes

# String
print("Shashi"[3]) # this will print 's'
print("Shashi " + "Anand") #output Shashi Anand

# Integer
print(12 + 23) # output is 35
print("12" + "23")  # output is 1223
num1 = 23
num2 = 12
print(num1 + num2)


# float
num3 = 1.38009
print(num3)

# boolean
check = True
print(check)

num_char = len(input("What is Your Name "))
print(type(num_char)) # this will show type 'int'

# print("Your Name have "+ num_char + "characters") # throw an error because it can't concanate int and string

new_num_char = str(num_char)
print("Your Name have "+ new_num_char + " characters")
var = False
print("value of var is ", var)

val = int(input("enter a number.\n"))
str_val = str(val)
sum = int(str_val[0]) + int(str_val[1])
print(sum)

# BMI
height = float(input("Enter Your Height in m "))
weight = float(input("Enter Your Weight in Kg "))

# bmi = int(weight/(height ** 2))
bmi = round(weight/(height ** 2), 2) # this is the another way to do this.
# print(8//3) this will print 2 which is type int
# bmi = (weight//(height ** 2)) but this one is type float
print("Your BMI : ", bmi)

print(f"Your Height is {height} m, Your Weight is {weight} Kg and Your BMI is {bmi}")
