x=eval(input())
for n in range(26):
    p=0
    num=ord('a')+n
    ah=chr(num)
    for m in x:
        p=m.count(ah)+p
    if p!=0:
        print(ah+",%d"%p)
