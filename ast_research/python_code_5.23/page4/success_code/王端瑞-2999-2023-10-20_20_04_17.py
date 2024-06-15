stext = input()

n,m = eval(input())

str = ""

for i in stext:

    if i == " ":

        str+=","

    else:

        str+=i

ls1 = str.split(',')

ls1[n],ls1[m] = ls1[m],ls1[n]

print(ls1)
