def search(nums)
     for x in nums:
         if count(x)>len(nums)//2:
             return(x)
             break
         else:
             continue
         print"False"

   





nums = eval(input())
y = search(nums)
print(y)


