def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(n):
    a = []
    s = str(n)
    for x in range(n):
        a.append(s*(x+1))
    print(sum(map(int,a)))
main()

