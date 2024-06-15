a=eval(input())
cubes=[x for x in range(1,a+1)]
'''b=cubes
f=cubes[0]
for x in range(a-1):
    b[x]=cubes[x+1]
b[a-1]=f
print(b)'''
b=cubes
c=b[0]
b.insert(-2,c)
b.pop(0)
print(b)
