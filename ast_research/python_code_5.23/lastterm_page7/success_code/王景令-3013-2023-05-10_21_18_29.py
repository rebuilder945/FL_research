a = input()
dic = {}
while a != 'ok':
    b,c = a.split()
    dic['b'] = eval(c)
    a = input()
ls1 = list(dic.keys())
ls1.sort()
ls2 = list(dic.values())
ls2.sort()
if 'India' not in ls1:
    print('no')
print(sum(ls2))

