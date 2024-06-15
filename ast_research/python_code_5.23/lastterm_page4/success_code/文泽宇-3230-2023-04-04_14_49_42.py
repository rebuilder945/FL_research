lst = eval(input())
lst.sort()
lst = lst[::-1]
s = "".join(map(str,lst))
print(s)
