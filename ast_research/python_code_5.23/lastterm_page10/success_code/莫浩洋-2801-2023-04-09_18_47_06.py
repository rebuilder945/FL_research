# a  =  input()
# b  =  input()
# la  =  len(a)
# lb  =  len(b)
# #建立二维列表，行数la+1，列数lb+1,初值为0
# res  =  [[0 for i in range(la+1)] for x in range(lb+1)]
# lc  =  []
# mmax  =  0
# for  i  in  range(1,  la+1):
#       for  j  in  range(1,  lb+1):
#             if  a[i-1]  ==  b[j-1]:
#                   res[i][j]  =  res[i-1][j-1]  +  1
#                   if res[i][j]>mmax:
#                         mmax=res[i][j]
                        
# print(mmax)#矩阵算法思路：把两个字符串分别以行和列组成一个二维矩阵；比较二维矩阵中每个点对应行列字符中否相等，相等的话值设置为1，否则设置为0；通过查找出值为1的最长对角线就能找到最长公共子串。
# #为了进一步优化算法的效率，我们可以再计算某个二维矩阵的值的时候顺便计算出来当前最长的公共子串的长度，即某个二维矩阵元素的值由M[i][j]=1演变为M[i][j]=1 +M[i-1][j-1]，这样就避免了后续查找对角线长度的操作了。

# 取出第一个没有重复的字符
# d={}
# s=input()
# if len(s)==0:
#     print("None")
# else:    
#     for i in s:
#         d[i]=d.get(i,0)+1
#     for i in s:
#         if d[i]==1:
#             print(i)
#             break

# s=[]
# s2=input()
# for i in s2:
#     s.append(i)
# s1="abcdefghijklmnopqrstuvwxyz"
# for i in range(len(s)):
#     if s[i].isalpha():    
#         if s[i].islower():
#             l=s1.index(s[i])+1
#             s[i]=s1[26-l]
#         else:
#             s[i]=s[i].lower()
#             l=s1.index(s[i])+1
#             s[i]=s1[26-l]
#             s[i]=s[i].upper()
# print(s2)
# print(*s,sep="")

#变位词
# n=input()
# m=input()
# n1,m1=[],[]
# for i in n:
#     n1.append(i)
# n1.sort()
# for i in m:
#     m1.append(i)
# m1.sort()
# if n1 == m1:
#     print("True")
# else:
#     print("False")

#身份证校验
# n=input()
# l,su=len(n),0
# x=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# if l ==18:
#     for i in range(17):
#         su+=int(n[i])*x[i]
#     a=(12-su%11)%11
#     if a == 10:
#         a="X"
#     if a==n[-1] or a==int(n[-1]):
#         print("Correct")
# else:
#     print("Error")

#输出最长数字子串
"""
str1,str2,m=input(),"",0  #m用于判断是否全为英文
for i in range(len(str1)):
    str2+=str1[-i-1]     #以输出最后一个最长数字串
str2+="a"  #避免最后一位为数字时不识别
d={"q":0}
a=""
p=False
for i in str2:
    if i.isdigit():
        a+=i
        p=True
        m=1
    else:
        if p and (len(a)>d[max(d, key=lambda x: d[x])]):
            d[a]=len(a) 
            p=False
        a=""
str3,str4=max(d, key=lambda x: d[x]),""
for i in range(len(str3)):
    str4+=str3[-i-1]
if m ==0:
    print("No digits")
else:
    print(str4)"""

#密码强度
intensity=0
n=input()
if len(n)>=8:
    intensity+=1
for i in n:
    if i.isdigit():
        intensity+=1
        break
for i in n:
    if  i.islower():
            intensity+=1
            break
for i in n:
    if  i.isupper():
            intensity+=1
            break                              
co="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
for i in n:
    if  i in co:
            intensity+=1
            break     
print(intensity)

        
    

