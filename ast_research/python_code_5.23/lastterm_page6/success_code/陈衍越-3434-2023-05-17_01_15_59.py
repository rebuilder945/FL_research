def change(fcolor,dcolor):
    if(fcolor=='red'and dcolor=='blue')or(fcolor=='blue'and dcolor=='red'):
        return'purple'
    elif(fcolor=='red'and dcolor=='yellow')or(fcolor=='yellow'and dcolor=='red'):
        return'orange'
    elif( fcolor=='yellow'and dcolor=='blue')or(fcolor=='blue'and dcolor=='yellow'):
        return'green'
    return'error'
fcolor=input()
dcolor=input()
print(change(fcolor,dcolor))
