def search(nums:list):
      c=len(nums)//2
      s=None
      for x in nms:
           if nums.count(x)>c:
                s=x
      if s :
          reture s
      else:
          reture False





nums = eval(input())
y = search(nums)
print(y)


