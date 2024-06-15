chang = eval(input())
kuang = eval(input())
if chang == kuang:
    print("It's a square")
elif chang != kuang:
    print("It's a rectangle")
elif chang < 0 or kuang < 0:
    print("illegal data")

