dic={}
while True:
    s=input()
    if s=='q':
        break
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
lst=[]
for x,y in dic.items():
    lst.append([x,y])
    lst.sort(key=lambda x : x[1])
print('%s %i'%(lst[-1][0],lst[-1][1]))
