name = input()
sc_input = input()
sc = eval(sc_input)

ls = name.split(',')
ls2 = [list(pair) for pair in zip(ls, sc)]
print(ls2)
