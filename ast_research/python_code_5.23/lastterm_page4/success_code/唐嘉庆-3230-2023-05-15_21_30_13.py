a=eval(input())
a.sort(reverse=True)
c=''.join(str(i) for i in a)
if int(c)==0:
    print('0')
else:
    print(c)
