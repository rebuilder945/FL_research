def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    c=0
    for i in range(1,a+1):
        b=str(a)*i
        c+=int(b)
    print(c)
main()

