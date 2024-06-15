def search(nums):
      lst.sort(reverse=True)
      max=0
      now=1
      ans=1
      a=len(lst)-1
      for x in range(a):
           before=lst[x]
           after=lst[x+1]
           if after==before:
                ans=ans+1
           else:
                ans=1
           if ans>len(lst)//2
                return(lst[x])
           return False





nums = eval(input())
y = search(nums)
print(y)


