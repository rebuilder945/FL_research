a=eval(input())
b=[]
jishu=0
for i in a:
    if a.count(i)==1:
        b.append(i)
        jishu+=1
        if jishu==0:
            print('False')
        else:
            b.sort()
            c=",".join(map(str,b))
            print(c)
