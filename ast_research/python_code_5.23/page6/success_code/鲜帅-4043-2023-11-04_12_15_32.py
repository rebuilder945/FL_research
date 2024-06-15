a = eval(input())
ls1 = [chr(x) for x in range(ord('a'),ord('z')+1)]
ls2 = [0]*26
for i in a:
    for x in i:
        ls2[ord(x)-ord('a')]+=1
for i,x in zip(ls1,ls2):
    if x>0:
        print('%s,%d'%(i,x))
