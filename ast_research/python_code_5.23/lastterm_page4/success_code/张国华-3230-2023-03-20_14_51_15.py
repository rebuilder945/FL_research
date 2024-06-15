lst_str = input()
lst = eval(lst_str)
lst.sort(reverse=True)
res = ""
for num in lst:
    res += str(num)
print(int(res))


