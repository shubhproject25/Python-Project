import log
import train
import booking   
import func

#Main entry point for the Railway Management System.Handles the main menu loop and directs users to specific modules.
l=log.login()
while True:
    if l=="Passenger login successfull" or l=="ID created":
        print("\n--- Main Menu ---")
        print("1. TRAIN INFO")
        print("2. BOOK TRAIN")
        print("3. CANCEL TICKET")
        print("4. LOG OUT")
        s=int(input("enter choice : "))
        if s==1:
            tname=input("enter train name :").lower()
            print()
            print(train.train(tname))
        elif s==2:
            tname = input("Enter train name: ").lower()
            train = train.traindetails[tname]
            route = train['route']
            print("available stations :",route)
            st = input("Enter start station: ").lower()
            end = input("Enter end station: ").lower()
            seats = int(input("Enter number of seats: "))
            r = booking.book(tname,train.traindetails, st, end, seats)
            print(r)
        elif s==3:
            func.cancel()
        elif s ==4:
            print("Logging out")
            break
        else :
            print("invalid input")
    elif l=="Admin login successfull":
        print("\nAdmin Menu:\n1. ADD TRAIN\n2. VIEW ALL TRAINS\n3. REMOVE TRAIN\n4. LOG OUT")
        c = int(input("Enter choice: "))
        if c== 1:
            train.addtrain()
        elif c== 2:
            for i in  train.traindetails.keys():
                print()
                train.train(i)
        elif c==3:
            func.remove()
        elif c== 4:
            print("Logging out...")
            break
        else:
            print("Invalid choice.")
    else :
        break