str1 = input()
ls = []
ls2 = []
for x in str1:
    ls.append(x)
for i in range(0,len(ls)):
    if ls.count(ls[i]) == 1:
        ls2.append(ls[i])
if ls2 == []:
    print('None')
else:
    print(ls2[0])

