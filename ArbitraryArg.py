def f1(*arg):
  sum = 0
  max = -65000
  min = 65000
  for i in range(len(arg)):
    sum += arg[i]
    if( arg[i] < min):
      min = arg[i]
    if ( arg[i] > max ):
      max = arg[i]
  avg = sum/len(arg)
  print('sum is : ',sum)
  print('Average is : ',avg)
  print('Max is : ',max)
  print('Min is : ',min)
f1(1,2,3,4)
