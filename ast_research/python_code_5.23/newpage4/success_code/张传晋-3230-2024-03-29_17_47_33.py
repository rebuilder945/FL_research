
lst = eval(input())
lst.sort(reverse=True)
sum =''
for i in range(len(lst)):
    sum = sum + str(lst[i])
print(sum)
