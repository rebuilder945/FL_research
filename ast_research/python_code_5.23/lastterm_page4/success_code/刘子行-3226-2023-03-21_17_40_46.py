def search(a):
     m=[a.count(x) for x in set(a)]
     if max(m)>=len(a)//2:
          return max(m)
     else:
          return max(m)>=len(a)//2





nums = eval(input())
y = search(nums)
print(y)


