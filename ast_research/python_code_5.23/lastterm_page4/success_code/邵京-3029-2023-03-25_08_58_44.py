names=input ()
grades=eval(input())
nameslist=list(names)
fingrades=[x+y for x in nameslist for y in grades]
print(fingrades)

