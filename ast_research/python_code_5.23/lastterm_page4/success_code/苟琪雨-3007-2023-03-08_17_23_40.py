list1=eval(input())
a,b=map(int,input().split(','))
if a<b and b<len(list1):
    del list1[a:b]
    print(list1)
else:
    print('error')
