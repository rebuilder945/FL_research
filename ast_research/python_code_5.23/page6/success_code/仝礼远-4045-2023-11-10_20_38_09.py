n=eval(input())
def fen(n):
    if n>=90:
        return 'A'
    if 90>n>=80:
        return 'B'
    if 80>n>=70:
        return 'C'
    if 70>n>=60:
        return 'D'
    if n<60:
        return "E"
print(fen(n))
