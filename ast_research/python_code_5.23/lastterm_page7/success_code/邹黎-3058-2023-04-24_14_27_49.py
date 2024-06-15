from optparse import Values

lst=[]
dic={}
while True:
    a=input()
    if a=="q":
        break
    else:
        dic[a]=dic.get(a,0)+1
for x,y in dic.items():
    lst.append([x,y])
lst.sort(key=lambda x:x[1], reverse=True)

print("%s %d"%(lst[0][0],lst[0][1]))
