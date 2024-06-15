def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    g = []
    c = 0
    b = [a]
    for i in range(1,a+1):
        e = b*i
        d = "".join("%s"%id for id in e)
        f = int(d)
        g.append(f)
    print(sum(g))
main()

