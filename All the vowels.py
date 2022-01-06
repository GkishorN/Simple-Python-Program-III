s=input("Enter the string:").lower()
r=[0,0,0,0,0]
for i in s:
    if(i=="a"):
        r[0]=1
    elif(i=="e"):
        r[1]=1
    elif(i=="i"):
        r[2]=1
    elif(i=="o"):
        r[3]=1
    elif(i=="u"):
        r[4]=1
if(sum(r)==5):
    print("Accept the string")
else:
    print("Reject the string")
