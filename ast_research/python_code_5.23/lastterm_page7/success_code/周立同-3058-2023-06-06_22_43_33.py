a=input()
dic={}
while(a!="q"):
    if a not in dic.keys():
        dic[a]=1
    else:
        dic[a]=dic[a]+1  
    a=input()
for b in dic.keys():
    if dic[b]==c:
        print(b,c) 
