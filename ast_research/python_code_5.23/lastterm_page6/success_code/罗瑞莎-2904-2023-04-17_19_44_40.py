def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sums=[]
    i=0
    while i<a:
        x=str(a)*(i+1)
        sums.append(int(x))
        i+=1
    print(sum(sums))
main()

