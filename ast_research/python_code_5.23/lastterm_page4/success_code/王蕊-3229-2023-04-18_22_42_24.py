def search(y):
    for x in y:
        if (y.count(x) ==1):
            return x
nums  =  eval(input())
y  =  search(nums)
if y!=[]:
    print(y)
elif y==[]:
    print("False")

