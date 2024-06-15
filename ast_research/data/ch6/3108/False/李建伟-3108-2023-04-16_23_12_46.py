lst = eval(input())
s = str("".join(lst))
print(s)
lst1 = [chr(i) for i in range(97,123)]
for i in lst1:
    n = 0
    for j in s:
        if i == j:
            n+=1
    if n != 0:
        print(i+",",n)
