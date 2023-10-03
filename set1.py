set1 = {1, 2, 3, 4, 5, 5, 6, 7, 8}
print(set1)

set2 = {"shashi", 2.34, 423, True}
li = ["sun", False, 994, 4.55]
sli = set(li)
set3 = {(334, 34), 23, 454, 90, 98}
print(set3)
################# we cannot put any list and dictionary because of mutability

for element in set2:
  print(element)

# print(2.34 in set2) --> True
# print("gogo" in set2) #--> False

set2.add("jack")
print(set2)
