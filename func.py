import train

#Contains Admin functionalities such as Canceling, Removing trains.
def cancel():
    n=input("enter train name : ")
    if n not in train.traindetails:
        print("train not found")
    else:
        pn=int(input("enter pnr number (8 digits): "))
        print("Your ticket on pnr number ",pn," for train ",n, " has been canceled")
    return " "

def remove():
    name=input("enter train to remove : ").lower()
    if name not in train.traindetails:
        print("Invalid Train")
    else:
        train.train(name)
        del train.traindetails[name]
        print ("This train has been removed")