lst = eval(input())
sum = 0
for i in range(len(lst)):
    sum = sum + max(lst)*(10**(len(lst)-1))
    lst.remove(max(lst))
print(sum)
