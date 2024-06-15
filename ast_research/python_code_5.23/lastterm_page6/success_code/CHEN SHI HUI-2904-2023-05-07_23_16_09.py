def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    num=[]
    i=0
    while i<a:
        x=str(a)*(i+1)
        num.append(int(x))
        i=i+1
    print(sum(num))
main()

