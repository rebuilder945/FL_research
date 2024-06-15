ls = input().split(',')
n,m=map(int,input().split(','))
ls1=[]
if n>=len(ls) or (-n)<=(-len(ls)):
    print('error')
else:
    for i in range(m):
        ls.append(ls[n])
ls=[int(i) for i in ls]
print(ls)


