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
int_num = str(num_char)
print("Your Name have "+ int_num + "characters")
