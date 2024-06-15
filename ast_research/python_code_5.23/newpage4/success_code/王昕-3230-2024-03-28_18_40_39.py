# a=eval(input())
# a.sort(reverse=True)
# a_str="".join(a)
# b=int(a-str)
# print(b)
f=eval(input())
f.sort(reverse=True)
num=len(f)
m=""
for i in range(num):#一般指代着有限次的循环
    x=str(f[i])
    m=m+x
print(int(m))

