w=input()
dict={}
while w!='q':
    dict[w]=dict.get(w,0)+1
    w=input()
    
for i in w:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
sum=max(dict.values())
for k,v in dict.items():
    if v==sum:
        print(k,v)






