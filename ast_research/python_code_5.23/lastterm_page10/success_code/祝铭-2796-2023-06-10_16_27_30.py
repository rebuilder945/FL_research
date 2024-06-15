st = input()
lio = []
lit = []
con = 0 
let = 0
dig = 0
for x in st:
    if x in ['0','1','2','3','4','5','6','7','8','9']:
        lit.append(let)
        let = 0
        con += 1
        dig += 1
    else:
        lio.append(con)
        con = 0
        let += 1
if con != 0:
    lio.append(con)
s = 0
for i in lio:
    if i == 0 :
        s += 1
    elif i != 0 and i != max(lio):
        s += i
    else:
        break
if dig == 0:
    print("No digits")
else:
    print(st[s+1:s+max(lio)+1])
print(st)
