balance=1000
pin="9856"
print("===Welcome to ATM====")
entered_pin=input("Enter your pin:")
if  entered_pin==pin:
  while True:
    print("\n==ATM MENU==")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    choice=input("Enter your choice :- ")
    if choice=="1":
      print(f"your current balance is RS.{balance}")
    elif choice=="2":
      try:
        amount=float(input("Enter Deposite Amount.:-"))
        if amount>0:
          balance=balance+amount
          print(f"RS.{amount} is Deposited Successfully")
          print(f"your new balance is RS.{balance}")
        else:
          print("Invalid Amount")
      except ValueError:
        print("Invalid Input")
    elif choice=="3":
      try:
        amount=float(input("Enter withdraw Money."))
        if amount <=balance and amount>0:
          balance=balance-amount
          print(f"RS.{amount} withdraw successfully")
          print(f"Remaining balance is Rs.{balance}")
        elif amount>balance:
          print("Insufficient Balance")
        else:
           print("Invalid Amount")
      except ValueError:
        print("Invalid Input")

    elif choice=="4":
      print("Thank you for using ATM...")
      break 
  else:
    print("Invalid Choice..")
else:
  print("Incorrect PIN . ")   

      
