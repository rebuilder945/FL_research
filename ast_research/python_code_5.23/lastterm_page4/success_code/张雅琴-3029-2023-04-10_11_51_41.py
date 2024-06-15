names=[eval(input())]
grades=eval(input())
new=[x+y for x in names for y in grades]
print(new)
