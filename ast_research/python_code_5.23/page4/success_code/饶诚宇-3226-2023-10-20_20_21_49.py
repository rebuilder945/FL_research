def search(y):
      for x in y:
           if(y.count(x)>(len)//2):
                return x
      return False






nums = eval(input())
y = search(nums)
print(y)


