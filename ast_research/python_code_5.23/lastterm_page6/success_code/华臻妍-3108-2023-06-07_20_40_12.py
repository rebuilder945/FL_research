lst=(list(eval(input())))
count=[0]*26
for i in lst:
    for z in i:
        count[ord(z)-ord('a')]+=1
for i in range(26):
    if count[i]>0:
        print(chr(ord("a")+i),count[i],sep=",")
        #ord函数接受一个字符并返回一个整数，用于获取ASCII的值
        #chr函数用于接受一个数字并返回一个字符
