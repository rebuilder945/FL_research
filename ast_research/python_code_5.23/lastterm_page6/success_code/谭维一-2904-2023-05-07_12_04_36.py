def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    t = a
    p = 10
    while True:
        s += t
        if t >= a * (p // 10):
            break
        t = t * 10 + a
        p *= 10
    return s
main()

