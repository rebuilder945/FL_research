def shuixianhuashu(n):
    if n<100 or n>999:
        return False
    elif int(str(n)[0])**3+int(str(n)[1]**3)+int(str(n)[2]**3)==int(n):
        return True
    return False
a=eval(input())
for i in range(a):
    if shuixianhuashu(i):
        print(i)
    else:
        print("none")
