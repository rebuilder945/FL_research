def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for n in range(1,a+1):
        s = "".join([a]*n)
        s += s
        print(s)
main()

