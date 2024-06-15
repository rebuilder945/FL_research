def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    c =a
    for i in range(a):
        b.append(10**i*a*c)
        c-=1
    print(sum(b))
main()

