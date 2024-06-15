a = eval(input())
b = "".join(a)
lst =[]
lst1 = []
for i in range(0,len(b)):
    if ord(b[i]) not in range(97,123):
            False
    c = b.count(b[i])
    if b[i] not in lst:
        lst.append(b[i])
        lst1.append(c)
for x in range(0,len(lst)):
    print(("%s"",""%d")%(lst[x],lst1[x]))

