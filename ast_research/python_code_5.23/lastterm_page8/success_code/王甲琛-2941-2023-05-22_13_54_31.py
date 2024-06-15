def count_foreign(ids):
        a=[]
        num=0
        for x in ids:
            a.append(x)
        for i in a:
            if i[0] =='L':
                num+=1
        return(num)

origin=input().split()
print(count_foreign(origin))

