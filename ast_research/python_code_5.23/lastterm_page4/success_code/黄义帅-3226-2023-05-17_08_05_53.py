def search(lst):
       lstR=[x for x in lst if lst.count(x)>len(lst)//2]
       if lstR:
          return lstR[0]
       else:
          return False






nums = eval(input())
y = search(nums)
print(y)


