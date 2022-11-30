num=int(input("enter the any number....."))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if num==sum:
    print(num,"is a perfect number")
else:
    print(num,"is a not perfect number")











