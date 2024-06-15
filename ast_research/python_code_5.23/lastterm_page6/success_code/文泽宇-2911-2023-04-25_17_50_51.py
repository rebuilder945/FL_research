n = str(int(input()))
lst = [int(m) for m in n]
for i in range(0,len(lst)):
    lst[i] = (lst[i]+5)%10
lst = lst[::-1]
lst = [str(m) for m in lst]
wuhu = ''.join(str(m) for m in lst)
print(wuhu)

