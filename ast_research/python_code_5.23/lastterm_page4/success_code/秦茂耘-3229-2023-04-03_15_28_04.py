s = input().replace("[","").replace("]","")
s = list(set(s.split(",")))
res = []
for i in s:
    res.append(int(i))
res = sorted(res)
for i in range(len(res)):
    res[i] = str(res[i])
print(",".join(res))
