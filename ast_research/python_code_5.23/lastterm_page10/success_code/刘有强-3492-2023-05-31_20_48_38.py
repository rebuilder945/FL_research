a=str(input())
b=[]
for x in a:
    b.append(x)
    if b.count(x) >=2 :
        print(x)
        break
