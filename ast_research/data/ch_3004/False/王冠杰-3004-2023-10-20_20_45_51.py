a=eval(input())
b=[]
for x in a :
    for y in range(2,x) :
        if x%y!=0 :
            b.append(x)
            break 
print(b)
