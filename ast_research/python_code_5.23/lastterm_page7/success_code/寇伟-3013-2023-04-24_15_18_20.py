dic = {}
while True:
    a=input()
    if a == 'ok':
        break
    else:
        dic[a[0]]=eval(a[1])
ket = dic.keys()
va = dic.values()
print(ket)
print(va)
if 'india' in ket:
    print('ok')
else:
    print('no')
print(sum(va))


