lst=input().split(',')
a,b=map(int,input().split(','))
if  a>b:
    print("error")
else:
    for i in range(a,b):
        lst2=lst.pop(i)
        print(lst)

