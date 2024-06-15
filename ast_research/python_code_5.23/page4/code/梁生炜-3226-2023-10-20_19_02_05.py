def search(x):
      for a in x:
           if (x.count(a)>len(x)//2):
              return(a)
          else:
              return('False')





nums = eval(input())
y = search(nums)
print(y)


