ls1 = input().split(",")
ls2 = eval(input())
ls3 = [[ls1[i],ls2[i]] for i in range(len(ls2))]
print(ls3)
