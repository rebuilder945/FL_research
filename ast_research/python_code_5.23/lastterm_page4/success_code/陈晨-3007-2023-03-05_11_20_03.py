lst=eval(input())
r=input()
a,b=eval(r)
num=len(lst)
if b<=num-1 and a>=0:
    del lst[range(a,b)]
    print(lst)
else:
    print("error")
