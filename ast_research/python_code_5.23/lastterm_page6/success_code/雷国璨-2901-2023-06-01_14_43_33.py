a=0
jishu=0
eva=0
b='1'
while b!='#':
    b=input()
    if b!='#':
        a=eva(b)
    jishu+=1
    eva+=a
print("{}{}".format(jishu-1,eva-a))
