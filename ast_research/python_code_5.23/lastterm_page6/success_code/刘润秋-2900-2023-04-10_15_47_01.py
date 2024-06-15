def su(n):
  if n==2 or n==3:
    return 1
  if n>3:
     for i in range(2,n):
        if n%i==0:
            return 0
        else:
            return 1
def hui(n):
    n1=str(n)
    n2=n1[::-1]
    if n1==n2:
        return n
N=float(input())
if int(N)<1 or (N-int(N))>0:
    print("illegal input")
else:
    s=[]
    for x in range(2,int(N)):
        if su(x)==1 and hui(x)==x:
            s.append(x)
    for x in range(len(s)):
        print('%d'%s[x],end=' ')
