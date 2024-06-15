def search(x):
      a=0
      for x1 in x:
            if x.count(x1)>len(x)/2:
                a=x1
                if a!=0:
                     return a
                else:
                     return False





nums = eval(input())
y = search(nums)
print(y)


