def search(x):
      b=0
      for i in x:
            a=x.count(i)
            if a>len(x)//2:
               print(i)
               break
            else:
                b+=1
      if b == len(x):
            print("false")






nums = eval(input())
y = search(nums)
print(y)


