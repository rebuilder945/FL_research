s=input()
dic={}
while s!="q":
    dic[s]=dic.get(s,0)+1
    s=input()
lst=[]
for x ,y in dic.items():
    lst.append([x,y])
lst.sort(key=lambda x:x[1])
print("%s %d"%(lst[-1][0],lst[-1][1]))


            




