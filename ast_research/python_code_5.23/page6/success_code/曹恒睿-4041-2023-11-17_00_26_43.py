changdu = eval(input())
kuandu = eval(input())
if changdu <= 0 or kuandu <= 0:
    print("illegal data")
elif changdu == kuandu:
    print("It's a square")
else:
    print("It's a rectangle")
