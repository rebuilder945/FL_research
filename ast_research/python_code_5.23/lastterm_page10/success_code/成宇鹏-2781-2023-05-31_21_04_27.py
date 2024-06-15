def suan(s):
    xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    a = []
    for x in range(17):
        b = int(s[x])*int(xishu[x])
        a.append(b)
    n = sum(a)%11
    m  = (12 - n)%11
    if m == 10:
        m = "X"
    return m
def yanzheng(s):
    if len(s) != 18:
        print("Error")
    else:
        if s[-1] == suan(s):
            print("Correct")
        else:
            print("Wrong")
s = str(input())
yanzheng(s)
