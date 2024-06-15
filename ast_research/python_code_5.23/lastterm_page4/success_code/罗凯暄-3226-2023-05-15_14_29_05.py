def search(y):
     z=len(y)/2
     for x in y:
          if y.count(x)>z:
               return x
          else:
               return False





nums = eval(input())
y = search(nums)
print(y)


