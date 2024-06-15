def nums1(num):
    for i in range(2,num):
        if num % i ==0:
            return False
ls=eval(input())  
right=[]
wrong=[]
for i in ls:
    if i<2:
        wrong.append(i)
    elif i>=2 and nums1(i)==False:
        wrong.append(i)
    else:
        right.append(i) 
print(right)                     
