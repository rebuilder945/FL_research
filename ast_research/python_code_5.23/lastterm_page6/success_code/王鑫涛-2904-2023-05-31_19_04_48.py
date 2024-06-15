def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    for i in range(a):
        c=(str(a))*i
        b+=(eval(c))
    print(b)
main()

