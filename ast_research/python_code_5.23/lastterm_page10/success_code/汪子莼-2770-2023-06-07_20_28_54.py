s1,s2=input(),input()
if len(s1)!=len(s2):
    print("False")
else:
    for x in s1:
        if x not in s2 or s1.count(x)!=s2.count(x):
            print("False")
        else:
            print("True")
