def iterPower(base, exp = 0):
  n=1
  for i in range(exp):
    n*=base
  return n;
print iterPower(2,4) 
