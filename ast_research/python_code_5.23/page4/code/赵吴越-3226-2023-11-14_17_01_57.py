def search(y):
   for x in y:
      if y.count(x)>(len(y)//2):
         print x
      print False





nums = eval(input())
y = search(nums)
print(y)


