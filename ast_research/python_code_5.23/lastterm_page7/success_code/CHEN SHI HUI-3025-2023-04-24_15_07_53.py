w=input().split( )
dict={}
 
for i in w:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
sum=max(dict.values())
for k,v in dict.items():
    if v==sum:
        print(k,v)






