lst=eval(input())
a,b=map(int,input().split(','))
if  a<=len(a) and b<=len(a):
    for i in range(a,b):
        lst=lst.pop(i)
        print(lst)
else:
    print("error")

