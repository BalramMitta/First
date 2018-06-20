def integerDivision(x, a):
    count=0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5, 3))
