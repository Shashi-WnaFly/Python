dict1 = {
  "Bihar": "Patna",
  "Delhi": "New Delhi",
  "Madhya Pradesh": "Bhopal",
  "Goa": "Panaji"
}
dict2 = {
  ("tomato", "carrot"): "veggies",
  # {0,1}: "Binary Number", # TypeError: unhashable type: 'set'
  "fruits": ["Banana", "Apple"],
  "aves": ["parrot", "eagle"]
}

# print(dict1|dict2) # union operator
# dict1|=dict2 # augmented dict union operator
# print(dict1)

print(dict1["Delhi"])
# print(dict2[("tomato", "cabbage")]) reases a KeyError
# print(dict2.get(("tomato", "cabbage"))) does reases an error and print none
print(dict2.get("amphibians", "Not found"))

# dict3 = dict() # empty initialization
# dict4 = {}
# print(type(dict4)) 
# print(dict4)
# print(dict3)

# cityCode = [("Varanasi", 2342), ('Bhopal', 965)]
# dict5 = dict(cityCode)
# print(dict5)

pairWords = dict(hands="legs", cup="plate", table="chair")
print(pairWords.get("hands"))

# dict1["Goa"] = "panji" updating the key:value pair
# print(dict1)
# dict1["Uttrakhand"] = "Dehradun" assigning the key:value pair
# print(dict1)

# dict1.update(dict2)
dict1.update(assam="Dispur", ArunachalPradesh="Itanagar")
print(dict1)

dict4 = {**dict1, **dict2}
print(dict4)

val = dict4.pop("Goa")
print(val)
