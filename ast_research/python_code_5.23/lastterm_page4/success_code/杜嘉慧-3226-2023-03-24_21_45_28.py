def search(y):
       z=0
       for x in y:
             if y.count(x)>len(nums)//2:
                return(x)
             else:
                return("False")





nums = eval(input())
y = search(nums)
print(y)


