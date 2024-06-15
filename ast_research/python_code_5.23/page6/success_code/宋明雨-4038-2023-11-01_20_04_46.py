List = list(input())
En = []
Num = []
T =[]
El = []
for i in List:
    if ord(i) >= ord("a") and ord(i) <= ord("z"):
        En.append(i)
    elif ord(i) >= ord("A") and ord(i) <= ord("Z"):
        En.append(i)
    elif ord(i) >= ord("0") and ord(i) <= ord("9"):
        Num.append(i)
    elif i == " ":
        T.append(i)
    else:
        El.append(i)
print(len(En),len(T),len(Num),len(El))
