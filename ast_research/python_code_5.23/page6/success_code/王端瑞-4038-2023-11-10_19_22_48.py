ls = input()

ls1 = []

ls2 = []

ls3 = []

ls4 = []

for i in ls:

    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":

        ls1.append(i)
    
    elif i == " ":

        ls2.append(i)

    elif i in "0123456789":

        ls3.append(i)

    else:

        ls4.append(i)

print(len(ls1),len(ls2),len(ls3),len(ls4))
