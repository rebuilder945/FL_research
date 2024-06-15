a = input()
dic = {}
while a != 'ok':
    b,c = a.split()
    dic['b'] = eval(c)
    a = input()
ls1 = list(dic.keys())
ls2 = list(dic.values())
if 'India' not in ls1:
    print('no')
print(sum(ls2))

