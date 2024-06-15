lst=input().split()
GDP={}
key=[]
value=[]
while lst!=['ok']:
    GDP[lst[0]]=lst[1]
    key.append(lst[0])
    value.append(eval(lst[1]))
    lst=input().split()
key.sort()
value.sort()
def india(key):
    if 'India' not in key:
        return 'no'
    else:
        return 'yes'
def sum(value):
    he=0
    for i in value:
        he+=i
    return he
print(key)
print(value)
print(india(key))
print(sum(value))
