def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    s=0
    t=1
    m=a
    for i in range(a):
        s=s+a*t*m
        t=t*10
        m=m-1
    print (s)        
main()

