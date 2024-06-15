GDP={}
while True:
    ls=input()
    if ls=='ok':
        break
    else:
        ls=ls.split()
        GDP[ls[0]]==int(ls[1])
nations=list(GDP.keys())
value=list(GDP.values())
nations.sort();value.sort()
print(nations)
print(value)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(value))
