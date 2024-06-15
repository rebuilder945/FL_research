a = input()
b = input()
h1 = [x for x in a]
h2 = [x for x in b]
h1.sort()
h2.sort()
if h1==h2:
    return True
else:
    return False
