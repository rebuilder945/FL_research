a=[input()]
b=eval(input())
i=0
for i in range(len(a)):

    c=[a[i],b[i]]
    i+=1
    print(c,end=())
c=[c]   
del c[-1]
print(c)
