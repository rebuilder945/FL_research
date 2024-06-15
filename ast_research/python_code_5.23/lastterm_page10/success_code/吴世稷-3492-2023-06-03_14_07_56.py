str1 = input()
ls = []
for x in str1:
    if x.isalpha():
        ls.append(x)
for i in range(0,len(ls)):
    if ls.count(ls[i]) == 1:
        print(ls[i])
        break
