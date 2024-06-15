sb=input().split(',')
n,m=eval(input())
if n>len(sb) or m>len(sb):
    print("error")
else: 
    if n<=m:
        del sb[n,m]
    else:
        del sb[n,m,-1]
    print(sb)
