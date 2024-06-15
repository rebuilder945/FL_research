c1 = input()
c2 = input()
s1 = {c1, c2}
purpleset = {'red', 'blue'}
orangeset = {'red', 'yellow'}
greenset = {'blue', 'yellow'}
tricolor = {'red', 'blue', 'yellow'}
if c1 not in tricolor or c2 not in tricolor or c1 == c2:
    print("error")
elif s1 == purpleset:
    print("purple")
elif s1 == orangeset:
    print("orange")
else:
    print("green")

