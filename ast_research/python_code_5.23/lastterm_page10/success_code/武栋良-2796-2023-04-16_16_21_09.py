def panduan(n):
    flag = True
    for x in n:
        if x in [str(i) for i in range(10)]:
            break
    else:
        flag = False
def main():
    n = input()
    flag = panduan(n)
    if flag:
        la=[]
        for i in range(len(n)):
            s = ''
            if n[i] in [str(i) for i in range(10)]:
                s = s+n[i]
                for y in range(i+1,len(n)):
                    if n[y] in [str(i) for i in range(10)]:
                        s=s+n[y]
                    else:
                        break
                la.append(s)
        a = 0
        for x in la:
            b = len(x)
            if b>a:
                a = b
        lc= []
        for x in la:
            if len(x)==a:
                lc.append(x)
        print(lc[len(lc)-1])
main()




