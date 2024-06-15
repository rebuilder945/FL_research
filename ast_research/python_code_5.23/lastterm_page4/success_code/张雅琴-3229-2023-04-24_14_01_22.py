a=eval(input())
b=[]
for i in a:
    number=0
    for x in a:
        if i==x:
            number+=1
        if number==1:
            b.append(i)
    b.sort()   
    if b==[]:
        print("False")
    else:
        print(",".join(str(x1)for x1 in b))
