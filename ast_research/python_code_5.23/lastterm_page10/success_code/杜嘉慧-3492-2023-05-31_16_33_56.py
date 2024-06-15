st = input()
if bool(st) == False:
    print("None")
else:
    for x in st:
        if st.count(x) == 1:
            print(x)
            break

