ls = list(eval(input()))
tep = []
num = 0
for i in range(len(ls)):
    if ls[i]==0:
        num+=1
    else:
        tep.append(ls[i])
for i in range(num):
    tep.append(0)
print(tep)

