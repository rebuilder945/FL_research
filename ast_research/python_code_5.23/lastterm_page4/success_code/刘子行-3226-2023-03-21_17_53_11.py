def search(a):
     n=len(a)
     for x in set(a):
          if a.count(x)>=n//2:
               h=x
          else:
               h="False"
     return h





nums = eval(input())
y = search(nums)
print(y)


