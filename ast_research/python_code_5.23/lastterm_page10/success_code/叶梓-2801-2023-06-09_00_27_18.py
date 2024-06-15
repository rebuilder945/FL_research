a=input()
key=[0]*5
str1="~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\"
if len(a)>=8:
    key[0]+=1
for i in a:
    if key[1]==0 and i.isdigit():
        key[1]+=1
    elif key[2]==0 and i.islower():
        key[2]+=1
    elif key[3]==0 and i.isupper():
        key[3]+=1
    elif key[4]==0 and i in str1:
        key[4]+=1
    else:
        pass
print(key.count(1))
