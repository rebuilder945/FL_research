def su(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i==0:
           return 0
    return n
s=eval(input())
if s<0 or type(s)!=int:
     print("illegal input")
else:
    for i in range(1,s+1):
        t=su(i)
        while str(t)==str(t)[::-1]:
              break
              print(t)

