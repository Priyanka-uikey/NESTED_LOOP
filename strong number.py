n=int(input("enter the number"))
sum=0
tamp=n
while tamp>0:
    f=1
    i=1
    rem=tamp%10
    while i<=rem:
        f=f*i
        i=i+1
    sum=sum+f
    tamp=tamp//10
if sum==n:
    print("strong number")
else:
    print("not strong number")


