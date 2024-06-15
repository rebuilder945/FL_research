def count_foreign(ids):
        a=0
        for i in str(ids):
            if i== 'L':
                a+=1
        return a

origin=input().split()
print(count_foreign(origin))

