def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    m=[]
    for i in range(x):
        n=x*10**i
        m.append(n)
    print(sum(m))
        

main()

