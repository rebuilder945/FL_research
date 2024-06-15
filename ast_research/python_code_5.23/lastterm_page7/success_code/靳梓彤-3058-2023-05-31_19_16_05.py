dic={}
while True:
    sen=input()
    if sen=="q":
        break
    elif sen in dic:
        dic[sen]+=1
    else:
        dic[sen]=1
lst=[]
for x,y in dic.items():
    lst.append([x,y])
    lst.sort(key=lambda x:x[1])
print('%s %i'%(lst[-1][0],lst[-1][1]))

