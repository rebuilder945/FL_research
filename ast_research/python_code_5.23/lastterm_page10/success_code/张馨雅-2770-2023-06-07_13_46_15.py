s1=list(input())
s2=list(input())
s1.sort()
s2.sort()
if s1==s2:
    print('True')
else:
    print('False')
# dic1={}
# for i in s1:
#     dic1[i]=dic1.get(i,0)+1
# dic2={}
# for i in s2:
#     dic2[i]=dic2.get(i,0)+1
# if (dic1|dic2)==len(s1) and (dic1|dic2)==len(s2):
#     print('False')
# else:
#     print('True')
