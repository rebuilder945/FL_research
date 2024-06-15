lst=eval(input())
n,m=eval(input())
l=int(len(lst))
if n>l:
    print ("error")
elif m>l:
    print ("error")
elif n<=m:
    shu=m-n
    while shu>0:
        del lst[int(n)]
        shu-=1
    print (lst)
