print("                        _____________")
print("                         ATM SYSTEM")
print("                        _____________")      
print("Welcome User Press Y To Continue And Other Key To Exit")
op1=input(" :")
if op1=='Y' or op1=='y':
    count=0
    flag=0
    wd=0
    deposit=0
    bal=10000
    pin=[1234,4321,5678,7890]

    for j in range(0,5):
        a= int(input("Enter ATM Pin:"))
    
        for i in range(0,len(pin)-1):
            if a in pin:
                flag=1
                
            else:
                flag=0
        
        if flag==1:
            for l in range(0,100):
                print(" ")
                print("Press 1 for withdraw")
                print("Press 2 for Deposit")
                print("Press 3 for Bal.Equiry")
                print("Press 4 for Mini Statement")
                print("Press 5 for Exit")
                opt=int(input("Enter a Choise:"))
                if (opt==1):
                    print("-------Withdraw-----")
                    
                    amount=int(input("Enter Amount:"))
                    bal=bal-amount
                    print("Thanku")
                    wd=wd+1
                    widh=[]
                    widh.append(amount)
                    
                elif(opt==2):
                    print("-------Deposit------")
                    amount1=int(input("Enter Amount:"))
                    bal=bal+amount1
                    dop=[]
                    dop.append(amount1)
                    
                    print("Thanku")
                    deposit=deposit+1
                    
                   
                elif(opt==3):
            
                    print("--------Balance enquery-----")
                    print("Total balance:",bal)
                    
                elif(opt==4):
                    print("                            Mini statement")
                    
                   
                   
                    
                    print("_______________________________________________________________________")
                    print("Withdraw:","                    ",wd,"                   ",widh)
                    print("Deposit:","                     ",deposit,"                   ",dop)
                    print("Total Balance:",bal)
                        
                elif(opt==5):
                    print("")
                    if opt==5:
                        break
                print("___________________")
               
                print("Press to continue")
                op2=input(":")
                if op2=='y':
                    continue
                else:
                    break
                    
    
        elif(flag==0):
            
    
            print("Wrong Pincode")
            count=count+1
            if count==3:
                print("your syster is block")
                break
            
     
    
          
else:
    print("you were exit")


