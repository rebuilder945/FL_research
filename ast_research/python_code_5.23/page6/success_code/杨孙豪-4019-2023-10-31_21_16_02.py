a=eval(input())
a=str(a)
lst=list(map(int,a))

lst=[(i+5)%10 for i in lst]

bst=lst[::-1]

bst=[str(i)for i in bst]

x=(''.join(bst))
print(x)
