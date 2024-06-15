lst=eval(input())
num=len(lst)
new=[]
k=""
while len(lst)==0:
    new.append(max(lst))
    lst.remove(max(lst))
for x in range(len(new)):
    k=k+str(new[x])
print(k)
