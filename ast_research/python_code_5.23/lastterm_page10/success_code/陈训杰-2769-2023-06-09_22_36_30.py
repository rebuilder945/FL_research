st=input()
zmb='abcdefghijklnmopqrstuvwxyz'
zmb2='ABCDEFGHIJKLNMOPQRATUVWXYZ'
for i in range(0,len(st)):
    sum=0
    sum1=0
    for x in range(0,len(zmb)):
        if x in range(0,len(zmb)):
            if(st[i])==zmb[x]:
                sum=x+1
                break
            else:
                continue
    for y in range(0, len(zmb2)):
        if (st[i] == zmb2[y]):
            sum1=y+1
            break
        else:
            continue
    if (97 <= ord(st[i]) <= 122):
        yes=chr(122-sum+1)
        print(yes,end='')
    elif (65 <= ord(st[i]) <= 90):
        yesl = chr(90-sum1+1)
        print(yesl,end='')
