def how_many(D):
  c=0
  for i in D.keys():
    c+=len(D[i])
  return c
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print how_many(animals)     #prints 6
