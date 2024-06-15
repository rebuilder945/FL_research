ls=eval(input())
lt=[]
for i in ls:
    for x in ls:
        if x==i:
            lt.append(i)
            break
print(lt)
