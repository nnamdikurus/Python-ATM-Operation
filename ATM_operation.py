pi = 3.142

                            # ATM OPERATION


print("INSERT YOUR ATM CARD")

menu = input("Welcome to our ATM Menu:\nPress 1 to check Account Balance\nPress 2 to Deposit\nPress 3 to Withdraw\nPress 4 to buy airtime\nPress 5 to Exit\n")

if menu == '1':
    balance = 0
    print(f"Your Account balance is {balance}\n")

elif menu == '2':
    depo = int(input("Enter amount to deposit\n"))
    balance = 0
    balance += depo
    print(f"Your account balance is now {balance}")
    balance += depo

elif menu == '3':
    balance = 5000
    withdraw = int(input("Enter amount to withdraw\n"))
    balance = balance - withdraw

    if withdraw < balance:
        print(f"You have withdrawn {withdraw}, your account balance is {balance}")
    else:
        print("You have insufficient balance, please top up your account balance")

elif menu == '4':
    airtime_menu = input("Press 1 for MTN\nPress 2 for Glo\nPress 3 for Airtel\nPress 4 for Etisalat\n")
    if airtime_menu == '1':
        print("MTN RECHARGE")
        recharge_options = int(input("Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n"))
        if recharge_options == 1:
            print(f"Recharge of N100 was successful.")

        elif recharge_options == 2:
            print(f"Recharge of N200 was successful.")

        elif recharge_options == 3:
            print(f"Recharge of N500 was successful.")


        elif recharge_options == 4:
            print(f"Recharge of N1000 was successful.")

        else:
            print("You entered an invalid option. Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n")


    elif airtime_menu == '2':
        print("GLO RECHARGE")
        recharge_options = int(input("Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n"))
        if recharge_options == 1:
            print(f"Recharge of N100 was successful.")

        elif recharge_options == 2:
            print(f"Recharge of N200 was successful.")

        elif recharge_options == 3:
            print(f"Recharge of N500 was successful.")


        elif recharge_options == 4:
            print(f"Recharge of N1000 was successful.")

        else:
            print("You entered an invalid option. Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n")


    elif airtime_menu == '3':
        print("AIRTEL RECHARGE")
        recharge_options = int(input("Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n"))
        if recharge_options == 1:
            print(f"Recharge of N100 was successful.")

        elif recharge_options == 2:
            print(f"Recharge of N200 was successful.")

        elif recharge_options == 3:
            print(f"Recharge of N500 was successful.")


        elif recharge_options == 4:
            print(f"Recharge of N1000 was successful.")
            
        else:
            print("You entered an invalid option. Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n")


    elif airtime_menu == '4':
        print("ETISALAT RECHARGE")
        recharge_options = int(input("Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n"))
        if recharge_options == 1:
            print(f"Recharge of N100 was successful.")

        elif recharge_options == 2:
            print(f"Recharge of N200 was successful.")

        elif recharge_options == 3:
            print(f"Recharge of N500 was successful.")


        elif recharge_options == 4:
            print(f"Recharge of N1000 was successful.")
        else:
            print("You entered an invalid option. Press 1 for N100\nPress 2 for N200\nPress 3 for N500\nPress 4 for N1000\n")

    else:
        print("You entered an invalid option. Press 1 for MTN\nPress 2 for Glo\nPress 3 for Airtel\nPress 4 for Etisalat\n")

elif menu == '5':
        print("Take out your ATM card. Thank you for using our services!")



