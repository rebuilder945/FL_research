pc1=str(input())
pc2=str(input())
ls1=['red','blue']
ls2=['red','yellow']
ls3=['blue','yellow']
ls4=['red','blue','yellow']
if pc1==pc2 or pc1 not in ls4 or pc2 not in ls4:
    print('error')
if pc1 in ls1 and pc2 in ls1 and pc1!=pc2:
    print('purple')
if pc1 in ls2 and pc2 in ls2 and pc1!=pc2:
    print('orange')
if pc1 in ls3 and pc2 in ls3 and pc1!=pc2:
    print('green') 
