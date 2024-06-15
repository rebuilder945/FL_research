ls1 = input().split(",")
ls2 = input().split(",")
ls3 = [[ls1[i],ls2[i]] for i in range(len(ls2))]
ls3_sorted = sorted(ls3,key = lambda x:x[1])
print(ls3_sorted)
