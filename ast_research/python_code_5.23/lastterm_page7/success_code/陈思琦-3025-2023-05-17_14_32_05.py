a=input().split()
goods={}
for b in a:
    if goods.get(b,0)==0:
        goods[b]=1
    else:
        goods[b]+=1
    
a=max(goods.values())
for key,value in goods.items():
    if value==a:
        b=key
        print(b+"",a)
        
