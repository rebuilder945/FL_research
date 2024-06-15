a=eval(input())
b=[]
for x in a :
    if x > 3:
            if 0  in [x%i for i in range(2,x)]:
                    break
            else:
                if x not in b :
                    b.append(x)
                else:
                    break
   
    elif 1<x<4:
        b.append(x)
print(b)
