n=str(input()).split(',')
m=eval(input())
lst=[]
for i in range(0,len(n)):
    lst.append([n[i],m[i]])
print(lst)
