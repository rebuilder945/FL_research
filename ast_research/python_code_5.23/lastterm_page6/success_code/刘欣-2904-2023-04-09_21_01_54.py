def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x = 0
    s = 0
    m = a
    while x < a:
        b = a * (10 ** x)
        if x == 0 and a == 10: 
            b = a
        s += b * m
        x += 1
        m -= 1
    print(s)
main()

