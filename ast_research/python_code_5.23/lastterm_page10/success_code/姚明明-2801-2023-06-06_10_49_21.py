def qiang(mima):
    qiang=0
    s=r"~!@#$%^&*()_=-/,.?<>;:[]{}|\""#标志奇怪？
    Lower='abcdefghijklmnopqrstuywxyz'
    Upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums='1234567890'
    qiang_s=0
    qiang_l=0
    qiang_u=0
    qiang_n=0
    qiang_len=0
    if len(mima)>=8:
        qiang_len=1

    for x in mima:
        if x in s:
            qiang_s=1
        elif x in Lower:
            qiang_l=1
        elif x in Upper:
            qiang_u=1
        elif x in nums:
            qiang_n=1
    qiang=qiang_s+qiang_l+qiang_u+qiang_n+qiang_len

    return qiang
mima=input()
print(qiang(mima))



