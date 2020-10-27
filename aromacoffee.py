staff=input("set your password:")
val=5
sum=0
people=5
x=0
for people in range(5):
    
    x=int(input("Enjoy our new coffee flavour and give us ur rating from 1 to 5 "))
    print(x)
    sum=sum+x
    if x==1:
        print("terrible")
    elif x==2:
        print("bad")
    elif x==3:
        print("okay")
    elif x==4:
        print("good")
    elif x==5:
        print("toungeblaster")
    else:
        print("sorry enter number only between 1 to 5")
    print("thank you for ur feedback, do visit our aroma coffee shop")
print('enter your password to know the average\n')
pass1=input('password')
if(staff==pass1):
    avg=(sum)/val
    print("avg rating is:",avg)
else:
    print("password incorrect")

