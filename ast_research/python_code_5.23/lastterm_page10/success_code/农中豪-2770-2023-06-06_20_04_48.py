def judge(a,b):
    c=set()
    d=set()
    if len(a)!=len(b):
        print('False')
    else:
        for i in a:
            c.add(i)
        for j in b:
            d.add(j)
        if c==d:
            print('True')
        else:
            print('False')

a=list(input())
b=list(input())
judge(a,b)
