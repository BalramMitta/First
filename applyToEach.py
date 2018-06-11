def applyToEach(L,f):
  for i in range(len(L)):
    L[i]=f(L[i])
def inc(x):
  return x+1
def dec(x):
  return x-1
list=[1,2,3,4]
applyToEach(list,inc)
print list        #prints [2,3,4,5]
applyToEach(list,dec)
print list        #prints [1,2,3,4]
