lst=eval(input())
c=input().split(",")
a=eval(c[0])
b=eval(c[1])
if a>b or b>len(lst):
    print("error")
else:
    del lst[a:b]
    print(lst)
