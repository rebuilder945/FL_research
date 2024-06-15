def count_foreign(ids):
            b=5
            a=0
            for i in ids:
                b=i.find('L')
                if b==0:
                    a+=1
            return a


origin=input().split()
print(count_foreign(origin))

