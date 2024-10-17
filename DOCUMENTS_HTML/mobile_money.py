a="withdrawal"
b="deposit"
print("withdrawal")
print("deposit")
account=50000
cont={}
#transaction type
user_input=input("What is your transaction type: ")
for i in user_input: 
 #enter the amount to be withdrawn
 if user_input==a:#if the input is equivalent to withdrawal find amount to withdraw
    count=int(input(f"Input amount to be withdrawn: "))
    if account>=count:
      print(f"Your account balance is {account-count}")
    elif account<=count:
      print("Error!That cannot be done")
    else:
      print("That is a wrong transaction")  
    break
 #Entering amount to be deposited
 elif user_input==b:
    no_count=int(input(f"Input amount to be deposited: "))
    print(f"Your account balance is {account+no_count}")
    break
 else:
   print("Find a different service")   
   break

    
