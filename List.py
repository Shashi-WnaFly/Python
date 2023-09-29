list1 = [18,2,9,9,38,4,0,9]
list2 = ["sheep", "ox", "caterpillar", "Horse"]
list3 = [23, 23.34343, 'hello', 2+3j]

print(list1)
print(list2[-2])
print(list3[3])
print(list2[1:3])

l4 = ["Dragonfly", "Platypus"]

# list2[4:4] = l4
# list2.append(l4) ['sheep', 'ox', 'caterpillar', 'Horse', ['Dragonfly', 'Platypus']]
# list2.insert(4, l4) same as append output
# list3.remove("hello") takes the element as arguments
# list3.pop(1) takes index as argument and default remove last element
# del list1[4]

print(list1)

for i in range(len(list1)):
  print("list[{}] : {}".format(i, list1[i]))

# l5 = [char for char in "Hippopotamus" if char not in "aeiou"]
# print(l5)

# l6 = [(i,j) for i in list1 for j in list2]
# print(l6)

# list1.sort()
# list1.sort(reverse=True)
# print(list1)

def remainderSort(x):
  return x%10

list1.sort(key=remainderSort)
print(list1)

l7 = list2.copy()
print(id(l7))
print(id(list2))

list1.extend(list2)
print(list1)

print(list1.count(9))

list1.reverse()
print(list1)
