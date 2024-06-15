def count_foreign(ids):
            sum=0
            for i in ids:
                    en = i.find('L')
                    if en == 0:
                            sum+=1
            return sum

origin=input().split()
print(count_foreign(origin))

