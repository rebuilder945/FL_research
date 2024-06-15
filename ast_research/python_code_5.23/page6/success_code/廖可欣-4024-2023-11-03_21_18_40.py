def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    for i in range(1,a+1):
        a = str(a)
        s += int(a*i)
    print(s)
main()

