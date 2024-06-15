n,m=map(int,input().split(" "))
if m-n==3:
    if n>0:
        lst=[n,n+1,n+2]
        print(str(lst[0])+str(lst[1])+str(lst[2]),end=' ')
        print(str(lst[0])+str(lst[2])+str(lst[1]),end=' ')
        print(str(lst[1])+str(lst[0])+str(lst[2]),end=' ')
        print(str(lst[1])+str(lst[2])+str(lst[0]),end=' ')
        print(str(lst[2])+str(lst[0])+str(lst[1]),end=' ')
        print(str(lst[2])+str(lst[1])+str(lst[0]),end=' ')
    if n==0:
        print(str(lst[1])+str(lst[0])+str(lst[2]),end=' ')
        print(str(lst[1])+str(lst[2])+str(lst[0]),end=' ')
        print(str(lst[2])+str(lst[0])+str(lst[1]),end=' ')
        print(str(lst[2])+str(lst[1])+str(lst[0]),end=' ')
else:
    print("illegal input")
