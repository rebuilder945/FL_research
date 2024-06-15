lis=eval(input())
n,m=eval(input())
if n>len(lis) or n==len(lis):
    print("error")
else:
    while m-n>0:
        del lis[n]
        n+=n
    print(lis)
