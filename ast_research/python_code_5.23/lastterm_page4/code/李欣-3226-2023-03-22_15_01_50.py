def search(list):
      n=len(list)
      for i in list:
           m=list.count(i)
           if m>(n/2)
              return i
          else:
              return False





nums = eval(input())
y = search(nums)
print(y)


