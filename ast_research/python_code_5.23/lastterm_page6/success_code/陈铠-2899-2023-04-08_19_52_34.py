n,m=map(int,input().split())
if 0<=n<m<=9:
     lst=[]
     for a in range(n,m):
          for b in range(n,m):
               for c in range(n,m):
                    if a!=b and b!=c and a!=c:
                         num=str(a)+str(b)+str(c)
                         if num[0]!="0":
                              lst.append(num)
     print(" ".join(lst))        
else:
     print("illegal input")                 
