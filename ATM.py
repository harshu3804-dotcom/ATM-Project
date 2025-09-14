PIN=1234
AMOUNT=10000
print("Welcome to our ATM!")
print("1.Saving")
print("2.Current")
a=int(input("Select any of the above Option:-"))
if a==1 or a==2:
   print("click on next")
   print("Checkbalance=1        WithDraw=2")
   print("Deposit=3                  Changepin=4")
   print("                Exit==5")
   b=int(input("Select any of the above Option:-"))
   if b==1:
           print("Kindly Enter your Details below:-")
           s=int(input("Enter your Pin:"))
           if s==PIN:
               print("Your Account Balance is:- RS:-10,000")
           else:
               print("Please Enter Valid Pin")
   elif b==2:
               print("Kindly Enter your Details below:-")
               w=int(input("Enter WithDraw Amount:"))
               if w<=AMOUNT:
                   t=AMOUNT-w
                   print("1.To View Current Balance        2.To Exit")
                   r=int(input("select any of the above option:-"))
                   if r==1:
                      print("Your Account Balance now is",t)
                   else:
                      print("Thanks for Visiting") 
               else:
                   print("Sorry you don't have Sufficient Balance!")
   elif b==3:
               print("Kindly Enter your Details below:-")
               d=int(input("Enter your Deposit Amount:-"))
               if d<=1000:
                T=d+10000
                print("Total balance in Your Account",T)
               else:
                print("Your Deposit Amount is less")
   elif b==4:
               print("Kindly Enter your Details below:-")
               P=int(input("Kindly Enter your Old Pin:-"))
               if P==PIN:
                  print("Please Enter your New Pin Below:-")
                  n=int(input("Enter your New pin:-"))
                  print("your pin change")
               else:
                  print("Kindly Enter Valid Pin:-")
   elif b==5: 
               print("Exit")
               exit()
   else:
         print("Please select correct option:")
else:
       print("please Choose any one option")
   



    
