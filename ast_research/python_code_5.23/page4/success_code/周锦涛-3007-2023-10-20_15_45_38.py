ls=eval(input())
m,n=eval(input())
if max(m,n)>len(ls):
    print('error')
else:
    del ls[int(min(m,n)):int(max(m,n))]
    print(ls)
