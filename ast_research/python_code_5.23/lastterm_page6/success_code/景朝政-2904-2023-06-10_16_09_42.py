def main():
    a=int(input())
    calculate_sum(a)

def calculate_sum(a):
    s=0
    b=str(a)
    for i in range(1,a+1):
        s+=int(b*i)
    print(s)

main()

