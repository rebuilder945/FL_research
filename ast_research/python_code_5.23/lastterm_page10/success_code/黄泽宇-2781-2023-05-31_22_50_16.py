def id(x,n):   
    if len(x) != 17:
        return "Error"
    else:
        a=0
        for i in range(len(x)):
            x1=int(x[i])
            a += x1*d1[str(i)]
        b = a%11
        if d2[str(b)] == str(n):
            return "Correct"
        else:
            return "Wrong"
u=input()
p=list(u)
j=p.pop()
d1={'0': 7, '1': 9, '2': 10, '3': 5, '4': 8, '5': 4, '6': 2, '7': 1, '8': 6, '9': 3, '10': 7, '11': 9, '12': 10, '13': 5, '14': 8, '15': 4, '16': 2}
d2={'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3','10':'2'}
print(id(p,j))


