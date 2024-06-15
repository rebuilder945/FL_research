def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    m=0
    if a<10:
        for j in range(i+1):
            m+=10**j*a
        n+=m
    elif a<100:
        for j in range(i+1):
            m+=100**j*a
        n+=m
    print(n)
            
main()

