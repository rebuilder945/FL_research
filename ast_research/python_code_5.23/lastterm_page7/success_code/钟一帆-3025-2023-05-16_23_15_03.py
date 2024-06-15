# 编写一个程序读取未指定个数的字符串(以空格隔开)，找出出现次数最多的字符串及其出现次数。

# 如果出现次数最多的有多个字符串，按照字符串升序输出所有出现次数最多的字符串。

# 例如输入abc bcd abc bcd bbb,那么字符串"abc"和"bcd"出现的次数最多，2次，先输出abc 2，再输出bcd 2。
s=input().split(' ')
dic={}
v=[]
for i in s:
    a=s.count(i)
    dic[i]=a
    v.append(a)
b=list(dic.items())
b.sort(key=lambda x:x[0])
for i in b:
    if i[1]==max(v):
        print('%s %d'%(i[0],i[1]))

