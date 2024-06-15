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

#2
s = input()
s1=''
for i in range(len(s)):
    if ord('a')<=ord(s[i])<ord('a')+26:
        s1+=chr(ord('z')-ord(s[i])+ord('a'))
    elif ord('A')<=ord(s[i])<ord('A')+26:
        s1+=chr(ord('Z')-ord(s[i])+ord('A'))
    else:
        s1+=s[i]
print(s)
print(s1)













# #7
# a = input()
# b = input()
# if b in a:
#     a=a.replace(b,'')
# print(a)
