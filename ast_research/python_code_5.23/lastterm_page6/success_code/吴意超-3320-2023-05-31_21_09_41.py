m = int(input())
n = int(input())
if m < 0 or n < 0 or (m<0 and n < 0):
    print("illegal data")
elif m == n :
    print("It's a square")
else:
    print("It's a rectangle")
