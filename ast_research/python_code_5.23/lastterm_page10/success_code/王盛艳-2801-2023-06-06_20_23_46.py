mima = input()
qiangdu = [0,0,0,0,0]
ls = "\~!@#$%^&*()_=-/,.?<>;:[]}{|"
for i in mima:
    if "0" <= i <= "9":
        qiangdu[0] = 1
    elif "a" <= i <= "z":
        qiangdu[1] = 1
    elif "A" <= i <= "Z":
        qiangdu[2] = 1
    elif i in ls:
        qiangdu[4] = 1
if len(mima) >= 8:
    qiangdu[3] = 1
print(qiangdu.count(1))
