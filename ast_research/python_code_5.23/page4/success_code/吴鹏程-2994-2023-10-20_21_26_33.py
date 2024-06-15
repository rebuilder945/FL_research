from this import d


a=list(map(int,input().split(';')))
b,c=eval(input())
if (b+10<=len(a)):
    for x in range(c):
        d.append(a[b])
    a=a+d
    print(a)
else:
    print('error')



