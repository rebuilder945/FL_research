stext = input()

ls = input().split()

m = eval(ls[0])

n = eval(ls[1])

str = ""

for i in stext:

    if i == " ":

        str+=","

    else:

        str+=i

ls1 = str.split(',')

ls1[m],ls1[n] = ls1[n],ls1[m]

print(ls1)
