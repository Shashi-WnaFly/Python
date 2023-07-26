def prime_checker(num):
  for i in range(2, num+1):
    j = 2
    check = True
    while(j * j <= i):
      if(i%j == 0):
        check = False
      j += 1

    if(check):
      print(i)

prime_checker(100)
