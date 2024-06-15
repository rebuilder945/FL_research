alpl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpu = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cos = input()
print(cos)
co = []
for h in cos:
    co.append(h)
for i in range(len(co)):
    for j in range(len(alpl)):
        if co[i] == alpl[j]:
            co[i] = alpl[25-j]
            alpl.insert(25-j,0)
            alpl.remove(alpl[26-j])
    for k in range(len(alpu)):
        if co[i] == alpu[k]:
            co[i] = alpu[25-k]
            alpu.insert(25-j,0)
            alpu.remove(alpu[26-j])
for l in range(len(co)):
    print(co[l],end='')
