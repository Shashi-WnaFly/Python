import random

print(random.randint(100, 250)) # this will print between numbers including those.
print(random.random() * 9) # will print float less than 9
loveScore = random.randint(1, 100)
print(f"Your Love Score is {loveScore}")

animal = ["Lion", "Rhino", "wolf", "Tiger", "Peacock"]

print(animal[len(animal) - 1]) # this will print Peacock

print(animal[-2]) # this will print Tiger

animal.pop() # this will remove the last element
print(animal)

animal.reverse()
print(animal)
