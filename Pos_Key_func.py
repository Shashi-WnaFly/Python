import math

def greet_with(name, location):# positional arguments
  print(f"Namaste {name}.")
  print(f"What do you like in {location}?")

greet_with("Ankit", "Patna")

#################
def greet(location="Delhi", name="Govinda"):# Keyword arguments
  print(f"Namaste {name}.")
  print(f"What do you like in {location}?")

greet()

################
def no_of_cans(height, width, cover):
  area = height * width
  print(f"Number of cans will be use : {math.ceil(area/cover)}")

test_h = int(input("Enter the height of the wall."))
test_w = int(input("Enter the width of the wall."))
coverage = 5

no_of_cans(width=test_w, cover=coverage, height=test_h)
