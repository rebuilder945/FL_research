A = input()
B = input()
if eval(A) < 0 or eval(B) < 0 or A < B:
    print("illegal data")
elif eval(A) == eval(B):
    print("It's a square")
elif eval(A) != eval(B):
    print("It's a rectangle")
