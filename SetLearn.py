
set1 = {1, 2, 3, 4, 5, 5, 6, 7, 8}
# print(set1)

set2 = {"shashi", 2.34, 423, True}
# i think there is sorting or something algo works behinds the scene flo = True
# str, flo, int, boolean = set2; # unpacking

# print(int)
# li = ["sun", False, 994, 4.55]
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
dell = set2.pop()
print(dell)
# set2.add(tup); # but in this process whole object treat as a particular object
print(set2)

sett = {"Hello"};
sett1 = {"World!"};

# sett.update("World!");
# set3 = sett.union(sett1);
# print(set3);

# set2.remove("patna"); # it raises key error if element is not found

set2.discard("patna") # it not raises error
print(set2);

s1 = "Tutorialspoint"
s2 = set(s1)
s2.clear()
print(s2)

#_______________________________________________________________________
set3 = {5, 6, 7, 8, 9, 10, 11, 12, 13}

# set3.difference_update(set1) --> {9, 10, 11, 12, 13}
# set1.difference_update(set3) --> {1, 2, 3, 4}
# set4 = set3.difference(set1) --> it does the same thing but it return a new object
# print(set4)

# set3.intersection_update(set1) {8, 5, 6, 7}
# set4 = set1.intersection(set3)
# print(set4) {8, 5, 6, 7}

# set3.symmetric_difference_update(set1)
# set4 = set1.symmetric_difference(set3)
# print(set4) --> {1, 2, 3, 4, 9, 10, 11, 12, 13}

# set4 = set3-set1
# s = 0
# for ele in set4:
#   set1.add(ele)
#   s += 1


# print(f"{s} and {set1}")
# set4 = set3.union(set1)
# set3.update(set1)
# set4 = {*set1, *set3}
# print(set4)

# set4 = set3 set4 have the same order
# set4 = set3.copy() different address
# print(id(set4))

#################    Operators    ########################
# set4 = set1|set3 union operator
# print(set4)

# set4 = set1&set3 intersect operator
# print(set4)

# set4 = set3-set1 difference operator
# print(set4)

set4 = set1^set3
print(set4)
