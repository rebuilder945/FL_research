n = str(input())
ls=n.split(' ')
cao=ls.pop(0)
lst=list(map(int,ls))


lst=sorted(lst)
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(cao,lst[0],lst[1],lst[2],(lst[0]+lst[1]+lst[2])/3))
