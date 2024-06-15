a=input()
dic={}
c=0
while(a!="q"):
    if a not in dic.keys():
        dic[a]=1
    else:
        dic[a]=dic[a]+1
        if dic[a]>c:
            c=dic[a]   
    a=input()
for b in dic.keys():
    if dic[b]==c:
        print(b,c) 
