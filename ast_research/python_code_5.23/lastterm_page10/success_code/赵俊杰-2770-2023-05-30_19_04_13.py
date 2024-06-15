str1=input()
str2=input()
def P(str1,str2):
    p=0
    for x in str1:
        if x in str2:
            pass
        else:
            p=-1
        return p
if len(str1)==len(str2):
    if P(str1,str2)==0:
        print("True")
    else:
        print("False")
else:
    print("False")
    
        
