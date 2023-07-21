
print("Welcome to Pizza Deliveries!")
size = input("Which size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
sum = 0

if size == "S" or size == "s":
  sum += 15
elif size == "M" or size == "m":
  sum += 20
elif size == "L" or size == "l":
  sum += 25
else:
  print("Please enter correct value")
  
if extra_cheese == "Y" or extra_cheese == "y":
  sum += 1

if add_pepperoni == "Y" or add_pepperoni == "y":
  if size == "S":
    sum += 2
  else:
    sum += 3


print(f"Your final bill is ${sum}")
