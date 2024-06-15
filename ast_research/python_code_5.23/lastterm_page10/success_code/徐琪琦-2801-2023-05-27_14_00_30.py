# 编写程序，对输入的密码（长度不超过28）进行强度检测。密码强度规定为：
# 1）含有数字字符；
# 2)含有小写字母； 
# 3）含有大写字母；
# 4）密码长度不低于8；
# 5）至少含有~!@#$%^&*()_=-/,.?<>;:[]{}|\中的一个字符
# 规定密码满足上列任意条件即加一星，程序输出密码的星级
s = input()
star = 0
dic = {"digit":0,"lower":0,"upper":0,"zifu":0}
for i in s:
    if str(i).isdigit():
        dic["digit"] = dic.get("digit",0)+1
    elif str(i).islower():
        dic["lower"]=dic.get("lower",0)+1
    elif str(i).isupper():
        dic["upper"] =dic.get("upper",0)+1
    elif str(i) in ["~","!","@","#","$","%","^","&","*","(",")","_","=","-","/",",",".","?","<",">",";",":","[","]","{","}","|","\\"]:
        dic["zifu"] = dic.get("zifu",0)+1#注意\前面必须加个\表示转义字符！！
    else:
        pass
if dic["digit"] != 0:
    star+= 1
if dic["lower"] != 0:                 #注意，比如说，elif的存在说明可能lower这个键不存在，下面运行的时候就会出现keyerror
    star += 1
if dic["upper"] != 0:
    star +=1
if len(s) >= 8:
    star += 1
if dic["zifu"] !=0:
    star+=1
print(star)
