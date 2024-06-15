C = eval(input())
K = eval(input())
if C == K and C > 0:
    print("It's a square")
if C > K and K > 0:
    print("It's a rectangle")
if C < K and C > 0:
    print("It's a rectangle")
if C < 0 or K < 0:
    print("illegal data")
