def count_foreign(ids):
        a=[]
        for x in ids:
            a.append(x)
        for i in a:
            num=0
            print(i[0])
            if i[0] =='L':
                num+=1
        return(num)

origin=input().split()
print(count_foreign(origin))

