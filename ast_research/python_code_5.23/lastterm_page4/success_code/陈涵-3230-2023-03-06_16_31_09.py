num=eval(input())
num.sort()
num2=[num[x]*10**(x) for x in range(len(num)) ]
print(sum(num2))



