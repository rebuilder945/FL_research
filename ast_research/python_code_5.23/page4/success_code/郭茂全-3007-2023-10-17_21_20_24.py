lis=eval(input())
n,m=eval(input())
if m>len(lis) or m==len(lis):
    print("error")
else:
    while m-n>0:
        del lis[n]
        n+=n
print(lis)
