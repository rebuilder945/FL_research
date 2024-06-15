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

s=[]
s2=input()
for i in s2:
    s.append(i)
s1="abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if s[i].isalpha():    
        if s[i].islower():
            l=s1.index(s[i])+1
            s[i]=s1[26-l]
        else:
            s[i]=s[i].lower()
            l=s1.index(s[i])+1
            s[i]=s1[26-l]
            s[i]=s[i].upper()
print(s2)
print(*s,sep="")
