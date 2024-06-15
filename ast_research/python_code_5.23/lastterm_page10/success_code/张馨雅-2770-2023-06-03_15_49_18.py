s1=list(input())
s2=list(input())
dic1={}
for i in s1:
    dic1[i]=dic1.get(i,0)+1
dic2={}
for i in s2:
    dic2[i]=dic2.get(i,0)+1
if (dic1|dic2)==len(s1) and (dic1|dic2)==len(s2):
    print('False')
else:
    print('True')
