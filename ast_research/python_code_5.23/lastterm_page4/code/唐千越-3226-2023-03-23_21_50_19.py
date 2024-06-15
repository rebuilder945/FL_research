def search(a:list):
     n=len(a)
     b=n//2
     c=None
     for x in a:
           if a.count(x)>b:
              c=x
      if c :
           return c
      else:
           return False        





nums = eval(input())
y = search(nums)
print(y)


