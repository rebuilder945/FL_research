nums = eval(input())
prime=[]
for x in nums:
    if x>=2:
        for y in range(2,x,1):
            if x%y==0:
                break
        else:
            prime.append(x)
print(prime)

