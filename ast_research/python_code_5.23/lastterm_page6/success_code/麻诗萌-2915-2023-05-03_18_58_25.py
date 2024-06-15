n=eval(input())
def findnum(x):
    if x<100 :
        print('none')
    else:
        lst=[]
        for i in range(100,x):
            if i <1000:
                s=0
                for y in str(i):
                    s=s+int(y)**3
                if s==i:
                    lst.append(i)
        if lst==[]:
            print('none')
        else:
            for i in lst:
                print(lst)
findnum(n)
     



