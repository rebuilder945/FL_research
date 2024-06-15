lt=eval(input())
n,m=eval(input())

l=len(lt)
if n<=m<l:
    []=lt[n:m]
    print(lt)
else:
    print("error")


    
