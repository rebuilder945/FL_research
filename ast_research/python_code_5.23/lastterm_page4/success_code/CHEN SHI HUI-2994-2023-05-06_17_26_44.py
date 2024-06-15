l=list(eval(input()))
n,m=eval(input())

if n<len(l): 
        i=l[n]
        while m>0:
            l.append(int(i))
            m-=1
        print(l)
else:
    print('error')


