alpl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpu = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numl = ['0','1','2','3','4','5','6','7','8','9']
notes = '~!@#$%^&*()_=-/,.?<>;:[]\{|}'
cod = input()
s = 0
if len(cod) > 7:
    s += 1
for i in cod:
    if i in alpl:
        s += 1
        break
for j in cod:
    if j in alpu:
        s += 1
        break
for k in cod:
    if k in numl:
        s += 1
        break
for l in cod:
    if l in notes:
        s += 1
        break
print(s)
