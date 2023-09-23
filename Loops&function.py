def weekdays(n):
  match n:
    case 0: return "Monday"
    case 1: return "TuesDay"
    case 2: return "Wednesday"
    case 3: return "Thursday"
    case 4: return "Friday"
    case 5: return "Saturday"
    case 6: return "Sunday"
    case _: return "Invalid Day Number"

print(weekdays(4))
print(weekdays(21))

def access(user):
  match user:
    case "admin" | "manager": return "Full Access"
    case "Guest": return "Limited Access"
    case _: return "No Access"

print(access("manager"))

def intr(details):
  match details:
    case [amt, dur] if(amt < 10000):
      return amt*dur*10/100
    case [amt, dur] if(amt >= 10000):
      return amt*dur*15/100

print("interest is : ", intr([15000, 3]))

ren = '''
We use the range() function to get the sequence of numbers from 1 to n-1 and perform cumumulative multplication to get the factorial valUe.
'''
for char in ren:
  if char not in "aeiou":
    print(char, end="")

li = (12,23,23,4,45,56,2,78,97)
sum = 0
for n in li:
  sum += n

print(sum)
numbers = tuple(range(9))
print(numbers)
def factorial(N):
    if(N == 0): return 1
    return N*factorial(N-1)
# N = int(input("Enter any to gets its factorial : "))
# print("The Factorial of {} is {}.".format(N, factorial(N)))

t = [23,43,56,76,88,34]
ind = range(len(t))
for i in ind:
  print("index:", i, "value:", t[i])

di = {10:"ten", 20:"twenty", 30:"thirty", 40:"forty"}
for i in di:
  print(i,":", di[i])

for i in di.items():
  print(i)

for i, j in di.items():
  print(i,":",j)

for i in range(1,11):
  for j in range(1,11):
    k = i*j
    print("{:2d}".format(k), end=" ")
  print()

s='0'
while s.isnumeric()==True:
  s = input("Enter a number. ")
  if(s.isnumeric()==True):
    print(f'Your entered value {s}')
print("while loop is over")

u = "Python"
inde = len(u)-1
while(inde >= 0):
  for i in range(0, inde):
    print(" ", end=" ")
  for i in range(inde, len(u)):
    print(u[i],end=" ")
  print()
  inde-=1

def prime(n):
  if(n == 1 or n == 0): return False
  for i in range(2, n+1):
    if(i * i > n): return True
    if(n%i==0): return False

print(prime(12))
