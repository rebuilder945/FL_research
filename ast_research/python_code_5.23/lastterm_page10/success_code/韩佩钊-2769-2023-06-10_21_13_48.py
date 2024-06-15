str0 = input()
print(str0)
ls = list(str0)
ls1 = [chr(x) for x in range(97,123)]
ls2 = [chr(x) for x in range(65,91)]
for i in range(len(ls)):
    if ls[i] in ls1:
        ls[i] = ls1[len(ls1)-1-ls1.index(ls[i])]
    elif ls[i] in ls2:
        ls[i] = ls2[len(ls2)-1-ls2.index(ls[i])]
print("".join(ls))


