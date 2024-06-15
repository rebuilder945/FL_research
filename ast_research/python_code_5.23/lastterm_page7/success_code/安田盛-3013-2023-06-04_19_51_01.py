s=input().split() or "OK"
dic={}
while s!="ok":
    dic[s[0]]=int(s[1])
    s=input()
b=[]
a=list(dic.values())
for x,y in dic.items():
    b.append([x,y])
b.sort(key=lambda x:x[1])
print([b[x][0] for x in range(len(b))])
print([b[x][1] for x in range(len(b))])
if "India"in dic:
    print("yes")
else:
    print("no")
print(sum(a))



            




