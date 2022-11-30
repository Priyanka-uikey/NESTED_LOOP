m=int(input("enter the number"))
i=1
while i<=m:
    if m%2==0:
        a=m-2
        b=a-2
        print(a)
        print(b)
        break
    elif m%2!=0:
        a=m+2
        b=a+2
        print(a)
        print(b)
        break
    i=i+1
