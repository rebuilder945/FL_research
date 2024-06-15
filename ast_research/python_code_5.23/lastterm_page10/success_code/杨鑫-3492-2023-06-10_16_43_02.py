a = input()
if list(a)==[]:
    print("None")
else:
    for i in a:
        if type(i) == str:
            if a.count(i) == 1:
                b = i
                break

print(b)
