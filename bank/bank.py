def deposit():
    amount = float(input("enter amount to deposit: "))
    if amount < 0:
        print("*********************")
        print("amount should be greater than 0 $")
        print("*********************")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("enter amount to withdraw: "))
    if amount > balance:
        print("***********************")
        print("insuffient amount")
        print("*********************")
        return 0
    else:    
        return amount

def show_balance(balance):
    print("*********************")
    print(f"Your balance is $ {balance:.2f}")
    


def main():
    balance =0
    is_running = True

    while is_running: 
        print("******************************")
        print("     Banking program     ")
        print("******************************")
        print("1. Deposit ")
        print("2. Withdraw ")
        print("3. Balance")
        print("4. Exit")
        print("*********************")
        
        
        choice = int(input("enter your choice: "))
        
        
        if choice == 1:
            balance += deposit()
        elif choice == 2:
            balance -= withdraw(balance)
        elif choice == 3:
            show_balance(balance)
        else:
            exit()            
if __name__== '__main__':
    main()