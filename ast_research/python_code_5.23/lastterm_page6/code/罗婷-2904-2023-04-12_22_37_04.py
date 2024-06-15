def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    for i in range(a):
        m=0
        if a>9:
            for j in range(i+1):
                m+=10**j*a
            n+=m
        elif a>99:
            for j in range(i+1):
                m+=100**j*a
           n+=m
    print(n)
            
main()

