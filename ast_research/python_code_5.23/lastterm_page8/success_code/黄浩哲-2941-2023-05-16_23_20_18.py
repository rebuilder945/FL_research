def count_foreign(ids):
            y=0
            for x in ids:
                if x[0]=='L':
                    y+=1
            return y

origin=input().split()
print(count_foreign(origin))

