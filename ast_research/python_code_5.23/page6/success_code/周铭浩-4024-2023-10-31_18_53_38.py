def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    z=0
    for i in range(1,a+1):
        for y in range(i):
            z+=10**(y)*a
        x+=z
    print(x)

main()

