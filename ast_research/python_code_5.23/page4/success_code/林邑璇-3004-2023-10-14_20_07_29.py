a=eval(input())
nums=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53,57,59]
b=[]
for i in a:
    if i in nums:
       c=0 
    else:
        b.append(i)
print(b)
