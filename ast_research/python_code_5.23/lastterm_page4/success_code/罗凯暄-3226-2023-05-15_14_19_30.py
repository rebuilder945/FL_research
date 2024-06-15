def search(y):
     z=0
     for x in y:
          if y.count(x)>z:
               z=y.count(x)
     return x





nums = eval(input())
y = search(nums)
print(y)


