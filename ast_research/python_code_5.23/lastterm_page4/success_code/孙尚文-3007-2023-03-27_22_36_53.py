a=eval(input())
n,m=eval(input())
b=[]
if n>(len(a)) or m>(len(a)):
        print("error")
else :
    for x in range(n,m):
          b.append(x)
    for y in b:
          if y in a:
            a.remove(y)
    print(a)      
        



