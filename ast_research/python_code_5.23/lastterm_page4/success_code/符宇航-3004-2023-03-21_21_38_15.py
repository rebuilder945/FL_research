lst = eval(input())
sushu = []
for i in lst:
    if i >=2:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            sushu.append(i)
print(sushu)

