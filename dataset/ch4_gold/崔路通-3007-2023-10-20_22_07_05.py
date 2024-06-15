a=eval(input())
n,m=eval(input())
change=abs(m-n)
min=min(n,m)
max=max(n,m)

if max>len(a):
    print("error")
elif max<=len(a):
    del a[min:min+change]
    print(a)


    
