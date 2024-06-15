def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    x=a
    if a in range(100):
        for i in range(a):
            s+=x
            x=x*10+a
    if a in range(100,1000):
        for i in range(a):
            s+=x
            x=x*100+a
    print(s)
main()

