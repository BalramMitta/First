def biggest(D):
  c=0
  m=0
  for i in D.keys():
    if m<len(D[i]):
      m=len(D[i])
      c=i
  return c
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)
