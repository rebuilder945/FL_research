from re import I


a = eval(input())

ls = []

for i in range(a):

    x = i//100

    y = i//10%10

    z = i%10

    if x**3+y**3+z**3 == i:

        ls.append(i)

if ls == []:

    print("none")

else:

    for n in ls:

        print(n)
