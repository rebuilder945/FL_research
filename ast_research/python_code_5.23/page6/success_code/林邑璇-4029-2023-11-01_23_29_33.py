s=input()
s=s.split()
n,m=int(s[0]),int(s[1])
if -1<n<m-2:
    for i in range(n,m):
        for x in range(n,m):
            for u in range(n,m):
                if i!=x and i!=u and u!=x :
                    a=100*i+10*x+u
                    if a//100!=0:
                        print(a,end=" ")
else:
    print("illegal input")

