def search(y):
       z=0
       for x in y:
             if y.count(x)>=z:
                return(x)
             else:
                return("False")





nums = eval(input())
y = search(nums)
print(y)


