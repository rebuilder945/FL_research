le = list(range(1,eval(input())+1,1))
for i in range(1):
     le.insert(len(le),le[0])
     le.remove(le[0])
print(le)
