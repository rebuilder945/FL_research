a=[input()]
b=input()
i=0
for i in range(len(a)):

    c=[a[i],b[i]]
    i+=1
    print([c],end=())
    
del c[-1]
prin(c)
