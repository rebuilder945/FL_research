a=eval(input())
b=[]
for x in a :
    for y in range(2,x) :
        if x%2 ==1 :
            b.append(x)
        else :
            if x%y==0 : 
                b.remove(x)
                break
print(b)
