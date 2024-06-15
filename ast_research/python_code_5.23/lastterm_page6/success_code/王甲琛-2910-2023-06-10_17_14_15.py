high=eval(input())
n=eval(input())
lst=[high]
for i in range(n):
    high=high/2
    lst.append(high)
print(sum(lst))
