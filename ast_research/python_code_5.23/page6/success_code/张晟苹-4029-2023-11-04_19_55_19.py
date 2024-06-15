a,b=map(int,input().split(' '))
lst1=[i for i in range(a,b)]
lst2=[]
if len(lst1)<3:
    print('illegal input')
else:
    for x in lst1:
        for y in lst1:
            for z in lst1:
                if x!=y and x!=z and y!=z:
                    a=str(x)+str(y)+str(z)
                    print(int(a),end=' ')
