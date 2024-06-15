name=input().split(',')
num=input().split(',')
he=[]
for i in range(len(name)):
    jia=[name[i],num[i]]
    he.append(jia)
he=sorted(he, key=lambda x:x[1])
print(he)
