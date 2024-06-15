def search(x):
     n=len(x)
     a=n//2
     for i in x:
          if x.count(i)>a:
              return i
          if x.count(i)<=a:
              return False





nums = eval(input())
y = search(nums)
print(y)


