lst=[]
while True:
    a=(input())
    if a=="#":
        break
    else:
        lst.append(int(a))
print("%d %d"%(len(lst),sum(lst)))


