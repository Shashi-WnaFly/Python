tup1 = (1,2,3,4,5,6,7,8)
tup2 = ("ox", "cow", "buffalo", "camel")
tup3 = ("shasy", 23, 121.32, 3+3j, False)

# print(tup1[5])
# print(tup3[1:4])

# tup1[4] = 99 produce an error
# print(tup1)

# print(f"tup1 : {id(tup1)}") 
# l1 = list(tup1)
# l1.append(9)        tup1 object are different
# tup1 = tuple(l1)
# print(f"tup1 : {id(tup1)}")

# a, b, c, d, e, f, g = tup1  this will produce an error because of one variable is missing.
# a, b, c, d, e, f, g, h = tup1
# print(c) // ot --> 3

# x, *y, z = tup1
# print("x : {}, y: {}, z: {}".format(x , y , z)) --> x : 1, y: [2, 3, 4, 5, 6, 7], z: 8

# *i, j, k = tup1
# print(f"i: {i}, j: {j}, k: {k}") --> [1, 2, 3, 4, 5, 6], j: 7, k: 8

# for i in range(len(tup3)):  
#   print(f"tup[{i}] : {tup3[i]}")

################ tuple join ##################
tup4 = tup1 + tup2
print(tup4)

# tup5 = sum((tup1, tup3), ())
# print(tup5)

# tup6 , tup7 = tup1, tup2
# print(f"{tup6}\n{tup7}")

# tuple methods
print(tup1.count(1))
print(tup1.index(7))

tup8 = ()
for i in tup1:
  if i not in tup8:
    tup8 += (i,)

print(tup8)

sum = ()
for x in range(len(tup8)):
  r = random.randint(0, 50)
  sum += (r,)

print(sum)
