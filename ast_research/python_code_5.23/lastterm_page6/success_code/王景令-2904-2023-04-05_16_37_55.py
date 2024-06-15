def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = str(a)
    c = map(int,[b*(i + 1) for i in range(a)])
    print(sum(c))
main()

