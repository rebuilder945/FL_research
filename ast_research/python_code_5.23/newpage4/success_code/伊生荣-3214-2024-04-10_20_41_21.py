Is=eval(input())
a = len(Is)
for i in range(a):
    if Is[i] != 0:
        i += 1
    elif Is[i] == 0:
        del Is[i]
Is.append(0)
print(Is)
