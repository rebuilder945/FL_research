ls = list(eval(input()))
lscopy = ls.copy()
alone = []
flag = 1
for i in range(len(lscopy)):
    count = ls.count(lscopy[i])
    if count==1:
        alone.append(lscopy[i])
        # print(lscopy[i],sep=',')
        flag = 0

if flag:
    print("False")
else:
    print(*alone,sep=',')
