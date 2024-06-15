def search(a):
     n=len(a)
     b=n//2
     c=[]
     for x in range(n+1):
           if a.count(x)>=b:
              c.append(x)
              d=int(c)
              print(b)
        
        





nums = eval(input())
y = search(nums)
print(y)


