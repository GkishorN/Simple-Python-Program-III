s=input("Enter the string:")
c=s[0]
for i in s:
    flag=0
    for j in c:
        if(i==j):
            flag=1
    if(flag==0):
        c=c+i
print(c)
        
