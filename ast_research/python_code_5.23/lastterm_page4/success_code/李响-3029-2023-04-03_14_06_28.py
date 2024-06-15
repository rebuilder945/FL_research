a = list(input())
f = eval(input())
b = [x+y for x in a for y in f]
d = b[::len(a)]
print(d)
