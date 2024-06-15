def search(y):
    for x in y:
         if count(x)>count(y):
       return x
    else: 
           return False
nums  =  eval(input())





nums = eval(input())
y = search(nums)
print(y)


