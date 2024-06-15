def jjj(num):
    num=list(str(num))
    for i in range(len(num)):num[i]=str((int(num[i])+5)%10)
    num[::]=num[::-1]
    return ''.join(num)
num=input()
print(jjj(num))
