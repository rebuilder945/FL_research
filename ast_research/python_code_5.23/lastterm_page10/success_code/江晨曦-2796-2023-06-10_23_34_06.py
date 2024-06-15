# #1
# icard  =  input()
# birthday  =  icard[6:10]+'-'+icard[10:12]+'-'+icard[12:14]

# mask  =  icard[0:6]+'********'+icard[14:17]

# print(birthday)
# print(mask)

# #3
# def  main():
#         stra  =  input()
#         lista=  list(stra)
#         print(''.join(replace_stars(lista)))

# def  replace_stars(str_list):    #  将所有*号移动到数组的左侧
#         j  =  len(str_list)  -  1
#         for  i  in  range(len(str_list)  -  1,  -1,  -1):
#                 if  str_list[i]  !=  '*':
                        
#                         str_list[j],str_list[i]=str_list[i],str_list[j]

#                         j  -=  1
#         return  str_list

# main()

# #4
# a  =  input()
# b  =  input()
# la  =  len(a)
# lb  =  len(b)
# #建立二维列表，行数la+1，列数lb+1,初值为0
# res  =  [[0 for j in range(lb+1)]for i in range(la+1)]

# lc  =  []
# mmax  =  0
# for  i  in  range(1,  la+1):
#       for  j  in  range(1,  lb+1):
#             if  a[i-1]  ==  b[j-1]:
#                   res[i][j]  =  res[i-1][j-1]  +  1
#                   if(res[i][j]> mmax):
#                         mmax  =  res[i][j]
                        
# print(mmax)

'''----------------------------------------------------------------------------------------------------------------------'''

# #1
# s = input()
# b=0
# for i in s:
#     a = s.count(i)
#     if a==1:
#         print(i)
#         break
#     else:
#         b+=1
# if b==len(s):
#     print('None')

# #2
# s = input()
# s1=''
# for i in range(len(s)):
#     if ord('a')<=ord(s[i])<ord('a')+26:
#         s1+=chr(ord('z')-ord(s[i])+ord('a'))
#     elif ord('A')<=ord(s[i])<ord('A')+26:
#         s1+=chr(ord('Z')-ord(s[i])+ord('A'))
#     else:
#         s1+=s[i]
# print(s)
# print(s1)

# #3
# a=input()
# b=input()
# if len(a)!=len(b):
#     print('False')
# else:
#     c=0
#     for i in range(len(a)): 
#         if a[i] in b and b.count(a[i])==a.count(a[i]):
#             c+=1
#     if c == len(a):
#         print('True')        
#     else:
#             print('False')

# #4
# s=input()
# s1='7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2'.split('-')
# if len(s)!=18:
#     print('Error')
# else:
#     a=0
#     for i in range(17):
#         a+=int(s[i])*int(s1[i])
#     b=(12-a)%11
#     if s[-1]=='X':
#         if b==10:
#             print('Correct')
#         else:
#             print('Wrong')
#     else:
#         if eval(s[-1])==b:
#             print('Correct')
#         else:
#             print('Wrong')

#6
a=input()+'a'
c=0
lst=[str(x) for x in range(10)]
m=0
for i in range(len(a)-1):
    b=0
    if a[i] in lst:
        while a[i+b] in lst:
            b+=1
        if b>=m:
            m=b
            c=i
print(a[c:c+m])








# #7
# a = input()
# b = input()
# if b in a:
#     a=a.replace(b,'')
# print(a)
