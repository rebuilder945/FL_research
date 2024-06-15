n = str(int(input()))
lst = [int(m) for m in n]
for i in range(0,len(lst)):
    lst[i] = (lst[i]+5)%10
print(lst[::-1])
