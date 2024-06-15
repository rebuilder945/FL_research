def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    m=[]
    w=[]
    for i in range(x):
        n=x*10**i
        m.append(n)
        p=sum(m)
    for i in range(x):
        q=p//10**i
        w.append(q)
    print(sum(w))

        

main()

