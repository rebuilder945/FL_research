def search(n):
  f = "False"
  for x in n:
      cishu=n.count(x)
      zongshu=len(n)
      if cishu > zongshu//2:
        return x
  return f
      else:
        return False





nums = eval(input())
y = search(nums)
print(y)


