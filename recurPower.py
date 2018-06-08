def recurPower(base,exp=0):
  if exp==0 :
      return 1
  else :
      return recurPower(base,exp-1)*base
print recurPower(2,4)
