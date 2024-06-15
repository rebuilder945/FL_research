from imp import load_source


ls=eval(input())
a,b=eval(input())
m=max(a,b)
n=min(a,b)
if m>len(ls):
    print('error')
else:
    del ls[n:m]
    print(ls)

     
