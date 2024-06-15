lt=eval(input())
n,m=eval(input())

l=len(lt)
if n<=m<l:
    #[]=lt[n:m]不行？！
    for i in lt[n:m]:
        lt.remove(i)
    print(lt)
else:
    print("error")



