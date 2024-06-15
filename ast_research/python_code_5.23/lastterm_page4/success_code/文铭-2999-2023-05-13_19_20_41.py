ls = str(input()).split()
num = str(input()).split()
n = int(num[0])
m = int(num[1])
ls2 = [x for x in ls]
ls2[n] = ls[m]
ls2[m] = ls[n]
print(ls2)
