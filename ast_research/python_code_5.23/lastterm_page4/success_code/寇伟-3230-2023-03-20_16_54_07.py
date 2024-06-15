ls = eval(input())
ls.sort()
inte = 0
for i in range(len(ls)):
    inte += ls[i]*10**i
print(inte)

