def search(a):
     n=len(a)
     b=n//2
     c=[]
     for x in range(n+1):
           if a.count(x)>=b:
              c.append(x)
              print(c)
        
        





nums = eval(input())
y = search(nums)
print(y)


