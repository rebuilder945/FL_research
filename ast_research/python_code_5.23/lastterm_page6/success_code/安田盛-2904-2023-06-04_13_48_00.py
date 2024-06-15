def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=[str(a)*x for x in range(1,a+1)]
    for i in n:
        s+=int(i)
    print(s)

main()

