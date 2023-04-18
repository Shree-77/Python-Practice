"""
2.	Write a python program that helps in updating and displaying the user’s bank balance based on their type of transactions. 
"""
balance = float(input("Enter the account balance :  "))


operations = int(input(
    "Enter which operation you want to perform : \n 1.Deposit \n 2.Withdraw \n 3.view balance \n 4.exit \n" ))

if operations == 1:
    deposit=float(input("Enter the amount to be deposited : "))
    balance= balance+deposit
    print(" Deposit Successful!! /n Your current balance is " , balance)
elif operations==2:
    if balance<0:
        print("Insufficient balance")
    else : 
        Withdraw = float(input("Enter the amount to be withdraw : "))    
        balance-=Withdraw
        print(" Withdraw Successful!! /n Your current balance is " , balance)
elif operations==3:
    print("Your current balance is : " , balance)
else : 
    print("Enter the correct number")        