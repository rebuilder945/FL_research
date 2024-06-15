word=input()
eng_count=0
spl_count=0
num_count=0
oth_count=0
for i in word:
    if i==" ":
        spl_count=spl_count+1
    elif ord("a")<=ord(i)<=ord("z") or ord("A")<=ord(i)<=ord("Z"):
        eng_count=eng_count+1
    elif ord("0")<=ord(i)<=ord("9"):
        num_count=num_count+1
    else:
        oth_count=oth_count+1
print(eng_count,spl_count,num_count,oth_count)
