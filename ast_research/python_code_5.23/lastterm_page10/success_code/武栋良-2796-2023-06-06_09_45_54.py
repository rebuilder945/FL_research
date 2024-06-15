def panduan(n):
    flag = True
    for x in n:
        if x.isdigit():
            break
    else:
        flag = False
    return flag
def main():
    n = input()
    flag = panduan(n)
    if flag:
        la=[]
        for i in range(len(n)):
            s = ''
            if n[i].isdigit():
                s = s+n[i]
                for y in range(i+1,len(n)):
                    if n[y].isdigit():
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
        print(lc[-1])
    else:
        print('No digits')
main()




