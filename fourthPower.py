def fourthPower(n):
  def square(n):
    return n*n
  return square(square(n))
print fourthPower(2)
