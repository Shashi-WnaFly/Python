bucket = ["apple", "grapes", "pineapple", "mango"]
for i in bucket:
  # print(i)
  print(i + " great")
print(bucket)

#########
student_heights = input("enter the lists of student heights : ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
print(student_heights)
sum = 0

for j in student_heights:
  sum += j

avg = round(sum / len(student_heights))
print(avg)

###### find max
max = 0
student_scores = input("Enter Scores : ").split()
for score in range(0, len(student_scores)):
  student_scores[score] = int(student_scores[score])
for i in student_scores:
  if(i > max):
    max = i

print(max)

###### range
sumr = 0
for i in range(0, 101, 2):
  sumr += i

print(sumr)
