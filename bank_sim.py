print("Welcome to my bank! \n What action would you like to perform today?")



def withdraw(amount, balance):
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"You have succesfully withdrawn ${amount}. \n Your current balance is ${balance}")
    else:
        print("Invalid amount.")
    return balance

def deposit(amount, balance):
    if amount > 0:
        balance += amount
        print(f"You have succesfully deposited ${amount}. \n Your current balance is ${balance}")
    else:
        print("Invalid amount.")
    return balance
current_balance=0
while True:
    
    action=int(input("\n 1.Withdraw \n 2.Deposit \n 3.Check Balance \n 4.Exit \n>"))
    if not action >= 1 and not action <=4:
        print("Please enter a number among the options.")
    else:
        if action==1:
            amount=input("How much would you like to withdraw?")
            if not amount.isdigit():
                print("Please input a digit,")
            else:
                amount=int(amount)
                current_balance =  withdraw(amount, current_balance)
        elif action==2:
             amount=input("How much would you like to deposit?")
             if not amount.isdigit():
                print("Please input a digit,")
             else:
                amount=int(amount)
                current_balance=deposit(amount, current_balance)
        elif action==3:
            print(f"Your current balance is ${current_balance}")
        elif action==4:
            print("Thank you for banking with us!")
            break

