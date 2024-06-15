a=input()
a=a+'a'
ls=list(a)
number=0
answer=0
answer0=''
sr=''
for i in range(len(ls)):
    if ls[i].isnumeric() == True:
        sr=sr+ls[i]
        number=number+1
    else:
        if number>=answer:
            answer=number
            answer0=sr
        number=0
        sr=''
print(answer0)
