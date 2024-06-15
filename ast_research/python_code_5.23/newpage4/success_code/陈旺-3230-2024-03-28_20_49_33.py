a=list(input())
b=[]
a.remove("[")
a.remove("]")
c=((len(a)-1)/2)
for i in range(int(c)):
    a.remove(",")
for i in a:
    b.append(int(i))
b.sort(reverse=True)
map(str,b)
print("".join(map(str,b)))#把int列表中的元素堆积
