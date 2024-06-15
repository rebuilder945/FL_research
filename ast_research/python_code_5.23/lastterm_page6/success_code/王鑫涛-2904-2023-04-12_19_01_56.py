def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    for i in range(a):
        b.append(a*10**i)
    print(sum(b))
main()

