s=str(input())
def f(ls1,i):
    if ls1.count(ls1[i])==1:
        print(ls1[i])
    else:
        f(ls1,i+1)
if s=='':
    print('None')
else:
    ls1=s.split()
    f(ls1,0)

