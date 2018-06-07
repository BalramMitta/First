varA=7
varB=9
if isinstance(varA, str) or isinstance(varB, str) :
  print "String involved"
elif varA > varB :
  print "Bigger"
elif varA == varB :
  print "Equal"
else :
  print "Smaller"
