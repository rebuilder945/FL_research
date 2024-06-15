def search(m):
       for i in m:
             if m.count(i)>len(m)//2:
                 return i
       return False





nums = eval(input())
y = search(nums)
print(y)


