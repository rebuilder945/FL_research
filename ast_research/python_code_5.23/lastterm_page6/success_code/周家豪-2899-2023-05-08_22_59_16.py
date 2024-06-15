a,b=input().split(' ')
a,b=int(a),int(b)
lst2=[]
if a<0 or b>9 or b-a<=2:
    print('illegal input')
else:
    lst1=[i for i in range(a,b)]
    for i in lst1:
        for j in lst1:
            for k in lst1:
                if i!=j and j!=k and i!=k:
                    lst2.append(100*i+10*j+k)
for x in lst2:
    if x<100:
        lst2.remove(x)
print(' '.join(str(i) for i in lst2))
