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
        print(",".join(str(i)for i in b))
