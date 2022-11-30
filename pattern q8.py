n=int(input("enter the alpabet"))
i=0
while i<=n:
    k=ord("A")+i
    j=0
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
    i=i+1
    print()
    k=k+1