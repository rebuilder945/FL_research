a = input()
dic = {}
while a != 'ok':
    b,c = a.split()
    dic[b] = eval(c)
    a = input()
ls1 = list(dic.keys())
ls1.sort()
print(ls1)
ls2 = list(dic.values())
ls2.sort()
print(ls2)
if 'India' not in ls1:
    print('no')
elif 'India' in ls1:
    print('yes')
print(sum(ls2))

