# 编写一个程序，当在一个字符串中出现指定子串时就删除它。       
s = input().split("")
a = input()
ls = []
i = j = 0
end = 0
s1 = s.deepcopy()  #不可以一遍遍历一遍删除
def panduan(i,j,s,a): #判断每一项是不是相同
    if s[i] != a[j]:
        i += 1
if not " " in list(a):
    for i in s:
        if i != a:
            ls.append(i)
    print("".join(ls))
else:
    while i < range(len(s)) and j < range(len(a)):
        panduan(i,j,s,a)
        if s[i] == a[j]:
            end = i
            i+=1
            j+=1
            del s1[end - len(a)+1:end:]
        panduan(i,j,s,a)
    

    
    
