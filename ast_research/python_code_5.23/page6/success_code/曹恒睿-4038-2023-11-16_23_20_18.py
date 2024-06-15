n = input()
yingwenzifu = 0
kongge =0
shuzizifu = 0
qitazifu = 0
for x in n:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        yingwenzifu += 1
    elif x == " ":
        kongge += 1
    elif "0" <= x <="9":
        shuzizifu += 1
    else:
        qitazifu += 1
print(yingwenzifu,kongge,shuzizifu,qitazifu)
