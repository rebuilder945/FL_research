lst=eval(input())
a,b=map(int,input().split(','))
if  a<=len(lst) and b<=len(lst):
    for i in range(a,b):
        lst1=lst.pop(i)
    print(lst)
else:
    print("error")

