def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ans = 0
    t = a
    for i in range(1, a+1):
        ans += t
        t = t*10 + a
    print(ans)
main()

