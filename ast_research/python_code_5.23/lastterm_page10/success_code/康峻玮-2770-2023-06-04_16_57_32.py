string1 = input()
string2 = input()
if len(string1) != len(string2):
    print(False)
else:
    if string1.sort() == string2.sort():
        print(True)
    else:
        print(False)
