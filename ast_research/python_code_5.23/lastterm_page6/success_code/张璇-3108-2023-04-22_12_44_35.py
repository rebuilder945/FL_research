a=eval(input())
b={}
for x in a:
    for y in x:
        if y in b:
            b[y]+=1
        else:
            b[y]=1
lst=list(b.items())
lst.sort(key=lambda x:x[0])
for i in range(len(lst)):
    print("{},{}".format(lst[i][0],lst[i][1]))
