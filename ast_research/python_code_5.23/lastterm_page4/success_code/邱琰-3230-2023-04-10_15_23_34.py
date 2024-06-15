lst=eval(input())
lstnew=[]
k=""
while len(lst)!=0:
    lstnew.append(max(lst))
    lst.remove(max(lst))
for x in range(len(lstnew)):
    k=k+str(lstnew[x])
print(int(k))
