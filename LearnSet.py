set1 = {1, 2, 3, 4, 5, 5, 6, 7, 8}
print(set1)

set2 = {"shashi", 2.34, 423, True}
# i think there is sorting or something algo works behinds the scene flo = True
str, flo, int, boolean = set2; # unpacking

print(int)
li = ["sun", False, 994, 4.55]
# sli = set(li)
# set3 = {(334, 34), 23, 454, 90, 98}
# print(set3)
# ################# we cannot put any list and dictionary because of mutability

# for element in set2:
#   print(element)

# # print(2.34 in set2) --> True
# # print("gogo" in set2) #--> False

# set2.add("jack")
# print(set2)
# s = {}
# print(s)

tup = ("goa", "lisbon", "budapest");
set2.update(tup); # In this process each element add as a particular object
# set2.add(tup); # but in this process whole object treat as a particular object
print(set2)

sett = {"Hello"};
sett1 = {"World!"};

# sett.update("World!");
set3 = sett.union(sett1);
print(set3);

# set2.remove("patna"); # it raises key error if element is not found

set2.discard("patna") # it not raises error
print(set2);
