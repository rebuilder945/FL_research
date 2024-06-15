lst=eval(input())
lst.sort(reverse=True)
long=len(lst)
num=0
for i in range(long):
    num+=lst[i]*10**(long-i-1)
print(num)
