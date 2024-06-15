a=input().split()
goods={}
new={}
for b in a:
    if goods.get(b,0)==0:
        goods[b]=1
    else:
        goods[b]+=1
    
a=max(goods.values())
for key,value in goods.items():
    if value==a:
        b=key
        new[b]=a
dicnew=dict(sorted(new.items()))
for key,value in dicnew.items():
    print(key+'',value)
        
