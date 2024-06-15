n=eval(input())
list1=[]
if n>1 and isinstance(n,int):
    for x in range(2,n):
        for y in range(2,x):
            if x%y==0:
                break
        else:
            if str(x)[::]==str(x)[::-1]:
                list1.append(x)
                break
    print(*list1,sep=" ")
else:
    print("illegal input")
