def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    c=0
    for i in range(1,x+1):
        d=str(x)*i
        c+=int(d)
    print(c)
main()

