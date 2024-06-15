def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    d=0
    c=a
    for j in range(1,c+1):
        m=0
        while True: 
            if j >0:
                e = a * (10**(int(a/10+1)) )** (j - 1)
                m=m+e
                j=j-1
            else:
                break
        d=d+m


    print(d)
main()

