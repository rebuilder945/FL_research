lst=[]
while True:
    a=input()
    if a!='#':
        lst.append(int(a))
    else:
        break
print('%d %d'%(len(lst),sum(lst)))
