k=int(input("enter the number"))
i=1
while k>0:
    b=1
    while b<i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=k*2-1:
           print(i,end=" ")
           j=j+1
    print()
    k=k-1
    i=i+1