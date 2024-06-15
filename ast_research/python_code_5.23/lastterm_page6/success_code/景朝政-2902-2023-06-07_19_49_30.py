n=input()
son1, son2, mot1, mot2 = 2, 3, 1, 2
son3, mot3 = 0, 0
Sumall = son1 / mot1 + son2 / mot2
for i in range(n-2):
    son3 = son1 + son2
    mot3 = mot1 + mot2
    son1, son2 = son2, son3
    mot1, mot2 = mot2, mot3
    Sumall += son3 / mot3
 
print("%.4f", Sumall)
