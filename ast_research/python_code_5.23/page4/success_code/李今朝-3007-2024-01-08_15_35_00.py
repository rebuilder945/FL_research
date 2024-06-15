lst=eval(input())
a,b=map(int,input().split(','))
if  a>b:
    print("error")
if  a>len(lst) or b>len(lst):
    print("error")
else:
    for i in range(a,b):
        lst2=lst.pop(i)
        print(lst)

