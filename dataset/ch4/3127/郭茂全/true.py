n=eval(input())
x=0
if n==1:
    list=[1]
else:
    list=[x+1 for x in range(0,n)]
list.remove(1)
list.append(1)
print(list)
