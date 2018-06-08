def gcdIter(a,b):
  if a<b:
    g=a
  else:
    g=b
  while a%g!=0 or b%g!=0:
    g-=1
  else:
    return g
print gcdIter(12,13)
