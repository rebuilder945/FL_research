a=eval(input())
n,m=eval(input())
b=[]
c=[]
if n>(len(a)) or m>(len(a)):
        print("error")
else :
    for x in range(n,m):
          b.append(x)
    for x in range(len(a)):
          c.append(x)
    for y in b:
          c.pop(b)
    print(c)      
        



