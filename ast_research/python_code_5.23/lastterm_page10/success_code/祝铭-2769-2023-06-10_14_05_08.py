alpl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpu = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
co = input()
print(co)
col = []
for i in range(len(co)):
    for j in range(len(alpl)):
        if co[i] == alpl[j]:
            co[i] = alpl[-j-1]
    for k in range(len(alpu)):
        if co[i] == alpu[k]:
            co[i] = alpu[-k-1]
print(co)
