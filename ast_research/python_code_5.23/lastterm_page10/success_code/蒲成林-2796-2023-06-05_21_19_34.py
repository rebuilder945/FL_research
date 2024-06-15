# s = input()
# if s == "":
#     print("None")
# else:
#     for c in s:
#         if s.count(c) == 1:
#             print(c)
#             break
#     else:
#         print("None")



# a=" abcdefghijklmnopqrstuvwxyz "
# b=" ABCDEFGHIJKLMNOPQRSTUVWXYZ "
# w=input()
# z=''
# for i in list(w):
#     if i in a:
#         z+=a[26-a.index(i)+1]
#     elif i in b:
#         z+=b[26-b.index(i)+1]
#     else:
#         z+=i
# print(w+"\n"+z)

# s = input()
# print(s)
# result = ''
# for c in s:
#     if 'A' <= c <= 'Z':
#         result += chr(ord('A') + ord('Z') - ord(c))
#     elif 'a' <= c <= 'z':
#         result += chr(ord('a') + ord('z') - ord(c))
#     else:
#         result += c
# print(result)


# s1 = input()
# s2 = input()
# if sorted(s1) == sorted(s2):
#     print('True')
# else:
#     print('False')


# IDs=list(input())
# if len(IDs) != 18:
#     print('Error')
# else:
#     a=0
#     num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#     for i in range(17):
#         a+=int(IDs[i])*num[i]
#     numed=a%11
#     word={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
#     if word[numed]==IDs[17]:
#         print('Correct')
#     else:
#         print('Wrong')



a=list(input())
b=[]
c=[]
jishu=0
long=len(a)
while 1:
    if jishu==long-1:
        if a[jishu].isdigit():
            b.append(a[jishu])
            c.append(b)
            b=[]
        break
    elif a[jishu].isdigit() and a[jishu+1].isdigit():
        b.append(a[jishu])
    elif a[jishu].isdigit() and a[jishu+1].isdigit()!=True:
        b.append(a[jishu])
        c.append(b)
        b=[]
    jishu+=1
jishu=0
for i in c:
    if len(i)>jishu:
        jishu=len(i)
lst1=[]
for i in c:
    if len(i)==jishu:
        lst1=i
if len(lst1)!=0:
    for i in lst1:
        print(i,end="")
else:
    print("No digits")    
