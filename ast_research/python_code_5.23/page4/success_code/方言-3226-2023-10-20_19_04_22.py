def search(nums):
  n=len(nums)
  dic={}
  for i in nums:
    if i not in dic:
      dic[i]=1
    if i in dic:
      dlc[i]+=1
  for s in dlc.keys():
    if dlc[s]>(n//2):
      return s
  else:
    return False
    
       
      





nums = eval(input())
y = search(nums)
print(y)


