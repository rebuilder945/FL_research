str=input()
ls1=[]
ls2=[]
ls3=[]
ls4=[]
for i in str:
    if ord(i) in range(ord("a"),ord("z")+1) or ord(i) in range(ord("A"),ord("Z")+1):
      ls1.append(i)
    elif ord(i) in range(ord("0"),ord("9")+1):
        ls2.append(i)
    elif i==" ":
        ls3.append(i)
    else:
        ls4.append(i)
print(len(ls1),len(ls3),len(ls2),len(ls4))

