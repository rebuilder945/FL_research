s1,s2=input().split()
if len(s1)!=len(s2):
    print("False")
else:
    a=0
    for x in s1:
        if x not in s2 or s1.count(x)!=s2.count(x):
            print('False')
            a=1
        break
    if a==0:
        print("True")
