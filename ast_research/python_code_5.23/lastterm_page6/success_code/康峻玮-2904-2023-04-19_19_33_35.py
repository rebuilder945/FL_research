def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=str(a)
    ls=[]
    for x in a:
        q=a+a*x
        ls.append(q)
    w=eval(ls)
    e=sum(w)
    print(e)
         
main()

