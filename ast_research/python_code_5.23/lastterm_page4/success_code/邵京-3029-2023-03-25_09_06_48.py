names=input()
nameslist=names.split(',')
grades=eval(input())
fingrades=[x+y for x in names for y in grades]
print(fingrades)

