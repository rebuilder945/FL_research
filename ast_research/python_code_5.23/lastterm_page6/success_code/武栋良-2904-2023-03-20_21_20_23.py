def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = str(a)
    s = 0
    for i in range(0,a):
        d = b*i
        c = int(d)
        s = s+c
    print(s)
main()

