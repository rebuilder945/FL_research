def search(y):
     z=len(y)/2
     for x in y:
          if y.count(x)>z:
               print(x)





nums = eval(input())
y = search(nums)
print(y)


