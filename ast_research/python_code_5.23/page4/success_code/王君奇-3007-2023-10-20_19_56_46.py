sb=eval(input())
n,m=eval(input())
if n>len(sb)-1 or m>len(sb)-1:
    print("error")
else: 
    if n<=m:
        del sb[n,m]
    else:
        del sb[n,m,-1]
    print(sb)
