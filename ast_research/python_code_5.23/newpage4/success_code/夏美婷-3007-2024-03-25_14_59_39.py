list=eval(input())
n,m=eval(input())
a=len(list)
if n<0 or m>(a-1) or n>m:
    print("error")
else:
    for i in list[n:m]:#注意：
        list.remove(i)
    print(list)
