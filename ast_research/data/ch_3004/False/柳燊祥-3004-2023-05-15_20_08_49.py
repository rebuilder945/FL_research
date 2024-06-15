nums=eval(input())
list=[]
for x in nums:
    for i in range(2,x-1):
        if x>=0 and x%i!=0:
            list.append(x)
            print(list)
