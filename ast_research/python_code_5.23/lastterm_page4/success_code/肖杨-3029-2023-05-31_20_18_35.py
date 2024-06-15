t1 = list(input().split(","))
t2 = input().split(",")
t3 = []
for i in range(len(t2)):
    ti = t1[i]+t2[i]
    t3 += ti
    print(t3)

