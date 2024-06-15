def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    i=0
    while i<a:
        q=str(a)*(i+1)
        i=i+1
        ls.append(int(q))
    e=sum(ls)
    print(e)
         
main()

