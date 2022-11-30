i=1
even=0
odd=0
while i<=20:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
    i=i+1
print("total of even number is=",even)
print("total of odd number is=",odd)
