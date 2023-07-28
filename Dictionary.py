computer = {
  "keyboard" : "A device which known as pressing input device.",
  "mouse" : "A device which probably known as clicking and moving device"
}
# print(computer["mouse"])

computer["mouse"] = "A device which probably known as clicking and moving input device." # update the key value
# print(computer["mouse"])

computer["moniter"] = "A device which show the output to the user using gui." # adding a key and value

# print(computer) # print whole dictionary
# for thing in computer:
#   print(thing)
#   print(computer[thing])

####### coding challenge #######
student_scores = {
  "harry" : 81,
  "Ron" : 71,
  "Hermoine" : 99,
  "Draco" : 74,
  "Neville" : 62,
}

student_grades = {}
for key in student_scores:
  if(student_scores[key] > 90):
    student_grades[key] = "Outstanding"
  elif(student_scores[key] > 80 and student_scores[key] < 90):
    student_grades[key] = "Exceeds Expectations"
  elif(student_scores[key] > 70 and student_scores[key] < 80):
    student_grades[key] = "Acceptible"
  else:
    student_grades[key] = "Fail"

print(student_grades["harry"])
