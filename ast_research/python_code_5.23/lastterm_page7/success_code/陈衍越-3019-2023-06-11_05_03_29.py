information = input().split()
lst1 = ['name','english','python','math']
lst2 = [i for i in information]
lst3 = [eval(i) for i in lst2[1:4]]
lst3.sort(reverse = True)
#打包形成字典
dct = dict(zip(lst1,lst2))
avg = sum(lst3)/3
dct['avg'] = "%.2f"%avg

print(lst2[0],end=" ")
#print(list(dct.values())[0],end=" ")
print(*["%.2f"%i for i in lst3],end=" ")
print(dct['avg'])
#print(list(dct.values())[4])
