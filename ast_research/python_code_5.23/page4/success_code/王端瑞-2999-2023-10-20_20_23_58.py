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

print(ls1)
