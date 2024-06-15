def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    m=[]
    w=[]
    p=0
    for i in range(x):
        n=x*10**i
        m.append(n)
        p+=n
    for i in range(x):
        q=p//10**i
        w.append(q)
    print(sum(w))

        

main()

