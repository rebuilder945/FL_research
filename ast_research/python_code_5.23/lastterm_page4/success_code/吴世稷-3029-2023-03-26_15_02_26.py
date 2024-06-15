ls1 = input().split(",")
ls2 = eval(input())
print(ls1)
print(ls2)
ls3 = [[ls1[i],ls2[i]] for i in range(len(ls2))]
print(ls3)
