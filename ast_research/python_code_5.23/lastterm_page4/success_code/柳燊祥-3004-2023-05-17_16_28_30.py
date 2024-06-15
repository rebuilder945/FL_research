
nums=eval(input())
list1=[]
def sushu(n):
    for n in nums:
        if n>=2:
            for x in range(2,n):
                if n%x==0:
                    pass
        else:
            list1.append(n)
    print(list1)
sushu(nums)                

