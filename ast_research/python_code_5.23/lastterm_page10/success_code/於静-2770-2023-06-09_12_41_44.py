#先判断长度是否相等，再判断每个字母的个数是否相等
#字符串可以直接用count函数
def mian():
    s1=input()
    s2=input()
    print(hanshu(s1,s2))
def hanshu(s1,s2):
    if len(s1)==len(s2):
        for i in s1:
            if s1.count(i)!=s2.count(i):
                return False
        return True
    else:
        return False
mian()
      
      
