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


s1 = input()
s2 = input()
if sorted(s1) == sorted(s2):
    print('True')
else:
    print('False')

