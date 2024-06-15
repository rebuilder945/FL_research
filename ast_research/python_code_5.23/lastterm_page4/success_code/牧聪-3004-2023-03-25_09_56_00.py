list=eval(input())
nums=[]
for n in list:
    if n >= 2:       
        if n % (i for i in range(2, n)) != 0:
            nums.append(n)
    else:
        continue   
print(list)

