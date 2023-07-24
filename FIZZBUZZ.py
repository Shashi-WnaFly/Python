for cnt in range(1, 101):
  if(cnt % 3 == 0 and cnt % 5 == 0):
    print("FIZZBUZZ")
  elif(cnt % 3 == 0):
    print("FIZZ")
  elif(cnt % 5 == 0):
    print("BUZZ")
  else:
    print(cnt)
