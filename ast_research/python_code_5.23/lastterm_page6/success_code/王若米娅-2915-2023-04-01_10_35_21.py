n=400
lst2=[]
for i in range(n+1):
    if i<100 or i>999:
        continue
    else:
        lst=list(map(int,str(i)))
        c=lst[0]**3+lst[1]**3+lst[2]**3
        if i==c:
            lst2.append(i)
if lst2==[]:
    print("none")
else:
    for x in range(len(lst2)):
        print(lst2[x])


