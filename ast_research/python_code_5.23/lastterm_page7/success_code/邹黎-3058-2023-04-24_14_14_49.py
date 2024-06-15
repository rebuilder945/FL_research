from optparse import Values


dic={}
while True:
    a=input()
    if a=="q":
        break
    else:
        dic[a]=dic.get(a,0)+1
max=0
for i in list(dic.values()):
    if i >=max:
        max=i

for x in list(dic.keys()):
    b=dic[x]
   
    if b==max:
        print(x,max)
