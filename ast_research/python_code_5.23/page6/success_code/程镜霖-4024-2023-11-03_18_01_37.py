def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(a):
        for x in range(i):
            s=a*10**x
            x+=-1
    print(s)
main()

