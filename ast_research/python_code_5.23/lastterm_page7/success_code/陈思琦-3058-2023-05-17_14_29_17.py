
goods  =  {}
while True:
    b=input()
    if b!='q':
        if goods.get(b,0)==0:
            goods[b]=1
        else:
            goods[b]+=1
    else:
        a=max(goods.values())
        for key,value in goods.items():
            if value==a:
                b=key
                print(b+"",a)
        break
