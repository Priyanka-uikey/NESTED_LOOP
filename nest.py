

    
i=8
while i>=1:
    b=1
    while b<=8-i:
        print("",end=" ")
        b=b+1
        k=1
    while k<=i:
        if i%2!=0:
            print("*",end=" ")
        k=k+1
    print() 
    i=i+1