def search(x):
      b=0
      for i in x:
            a=x.count(i)
            if a>len(x)//2:
               return i
               break
            else:
                b+=1
      if b == len(x):
            return "False"






nums = eval(input())
y = search(nums)
print(y)


