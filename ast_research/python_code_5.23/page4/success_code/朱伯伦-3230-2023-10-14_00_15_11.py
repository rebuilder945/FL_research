list=eval(input())
list.sort(reverse=True)
m=""
for i in list:
    m=m+str(i)
print(int(m))
