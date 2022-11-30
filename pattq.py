n=5
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print('#',end=" ")
        else:
            print(j*j,end=" ")
        j+=1
    i+=1
    print()
b=4
k=b
while k>=1:
    j=1
    while j<=k:
        if k%2!=0:
            print('#',end=" ")
        else:
            print(j*j,end=" ")
        j+=1
    k-=1
    print()