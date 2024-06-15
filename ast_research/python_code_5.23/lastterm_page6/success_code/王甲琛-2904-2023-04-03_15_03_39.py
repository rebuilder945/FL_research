def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(a):
        x=i+1
        s=pow(10,a-x)*a*x+s
    print(s)
main()

