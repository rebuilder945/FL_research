def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    s=x+(x*10+x)+(x*100+x*10+x)
    print(s)
main()

