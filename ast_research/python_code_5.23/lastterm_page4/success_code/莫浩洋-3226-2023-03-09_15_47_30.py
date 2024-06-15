def search(x):
      for i in x:
          a=x.count(i)
          if a>len(x)//2:
               print(i)






nums = eval(input())
y = search(nums)
print(y)


