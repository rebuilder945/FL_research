def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    g = []
    c = 0
    for i in range(a):
        c = (a-i)*a*10**i
        g.append(c)
    print(sum(g))
main()

