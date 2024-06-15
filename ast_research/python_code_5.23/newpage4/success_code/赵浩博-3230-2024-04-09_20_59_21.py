ls=eval(input())
ls1=[]
for i in ls:
    ls1.append(i)
ls1.sort(reverse=True)
print(int(''.join(map(str,ls1))))

