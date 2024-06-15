n=eval(input())
jishu=0
for i in n:
    if i==0:
        del i
    jishu+=1
for x in range(jishu):
    n.append('0')
print(n)

