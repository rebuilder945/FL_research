a = input()
dic = {}
ls = []
i = 1
for x in range(len(a)):
    n = a[x]
    if n.isdigit():
        if x+1 != len(a):
            m = a[x+1]
            if m.isdigit():
                i += 1
            else:
                ls.append(i)
                dic[i] = x
                i = 1
        else:
            ls.append(i)
            dic[i] = x
            i = 1
k = dic[max(ls)]
print(a[k-2:k+1])
