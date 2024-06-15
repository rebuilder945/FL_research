def main():
    a=int(input())
    calculate_sum(a)

    print(calculate_sum(a))
def calculate_sum(x):
    b=0
    for i in range(x+1):
        c=x*(x-i)*10**i
        b+=c
    return b

main()

