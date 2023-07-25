import random

def print_No(n):
  for i in range(1, n+1):
    print(i)

print_No(23)

def print_no(m):
  while m >= 0:
    print(m)
    m -= 1

print_no(23)

word_list = ["advark", "baboon", "rhino"]
rand_var = random.choice(word_list)

input_var = input("Enter any letter please : ")

for i in range(0,len(word_list[rand_var])):
  print(input_var == word_list[rand_var][i])
