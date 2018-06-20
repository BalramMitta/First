def oddTuple(tup):
  return tup[0:len(tup):2]

test_tuple=('I', 'am', 'a', 'test', 'tuple')
print("Test tuple = ",test_tuple)
print("Odd tuple = ",oddTuple(test_tuple))
