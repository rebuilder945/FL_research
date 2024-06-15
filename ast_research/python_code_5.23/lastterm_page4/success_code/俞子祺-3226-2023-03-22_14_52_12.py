def search (x):
      m=0
      for x1 in x:
            if x.count(x1)>len(x)/2:
                m=x1
      if m!=0:
         return m
      elif y==0:
         return "False"





nums = eval(input())
y = search(nums)
print(y)


