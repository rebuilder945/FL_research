ls1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ls2 = []
for x in ls1:
    ls2.append(x.upper())
mima = input()
ls3 = []
for x in range(0,len(mima)):
    ls3.append(mima[x])
ls4 = ls3.copy()
for i in range(0,len(ls3)):
    if ls3[i] in ls1:
        for j in range(0,len(ls1)):
            if ls3[i]==ls1[j]:
                ls4[i] = ls1[25-j]
    elif ls3[i] in ls2:
        for j in range(0,len(ls2)):
            if ls3[i]==ls2[j]:
                ls4[i] = ls2[25-j]
print("".join(ls3))
print("".join(ls4))
