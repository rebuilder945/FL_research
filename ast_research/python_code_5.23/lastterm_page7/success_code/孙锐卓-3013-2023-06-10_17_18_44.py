a=input()
dict = {}
while(a != 'ok'):
    a = a.split()
    dict[a[0]] = int(a[1])
    a=input()

ls1=list(dict.keys())
ls2=list(dict.values())
ls1.sort()
ls2.sort()
print(ls1)
print(ls2)
if("India" in dict):
    print('yes')
else:
    print("no")
print(sum(dict.values()))

