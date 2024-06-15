a = eval(input())
list0 = []
for m in range(a + 1):
    A = str(m)
    B = []
    for i in range(len(A)):
        b = m
        for _ in range(i):
            b = b // 10
        b = b % 10
        B.append(b)
    for i in range(len(B)):
        B[i] = pow(B[i],3)
    if sum(B) == m:
        list0.append(m)
list0.pop(0)
list0.pop(0)
if list0 == []:
    print("none")
else:
    for i in range(len(list0)):
        print(list0[i])


