def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    for i in range(a):
        m=0
        for j in range(i+1):
            m+=10**j*a
        n+=m
    print(n)
            
main()

