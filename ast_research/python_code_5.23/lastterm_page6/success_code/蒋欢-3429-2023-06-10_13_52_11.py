a=input()
num=[]
letter=[]
space=[]
qita=[]
for x in a:
    if x.isnumeric()==True:
        num.append(x)
    elif x.isspace()==True:
        space.append(x)
    elif ord(x) in range(ord('a'),ord('z')+1) or ord(x) in range(ord('A'),ord('Z')+1):
        letter.append(x)
    else:
        qita.append(x)
print("%d %d %d %d"%(len(letter),len(space),len(num),len(qita)))
