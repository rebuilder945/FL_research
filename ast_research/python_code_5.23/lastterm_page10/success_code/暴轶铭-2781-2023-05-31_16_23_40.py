n=input()
if len(n)!=18:
    print("Error")
else:
    n_check=n[17]
    W=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] 
    ncheck=["1","0","X","9","8","7","6","5","4","3","2"]
    n_awx=0

    for i in range(len(W)):
        n_awx = n_awx+int(n[i])*W[i]  

    n_check = n_awx%11
    if n_check != ncheck[n_check]:
        print("Wrong")
    else:
        print("Correct")
