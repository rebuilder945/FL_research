a=eval(input())
b=a.count(0)
for i in range(b):
	a.remove(0)
c=[0]*b
e=a+c
print(e)
