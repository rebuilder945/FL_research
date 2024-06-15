def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    i=0
    c=[]
    while i<a:
        x=str(a)*(i+1)
        c.append(int(x))
        i=i+1
        print(sum(c))

main()

