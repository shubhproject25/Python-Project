admin = {'aman': 'admin123','vikas': 'admin456'}
passenger= {'prateek': 'gvsprateek','surya': 'balasurya'}

#Manages User Authentication (Login/Signup).
def login():
    print("Login as:\n1. Admin\n2. Passenger\n3. Sign Up as Passenger")
    ch = int(input("Enter : "))  

    if ch == 1:
        u= input("Admin ID: ")
        p= input("Password: ")
        if admin.get(u) == p:
            return "Admin login successfull"
        else:
            print("Invalid ID")
            return "try again"
    elif ch == 2:
        u= input("Passenger ID: ")
        p= input("Password: ")
        if passenger.get(u) == p:
            return "Passenger login successfull"
        else:
            print("Invalid ID")
            return "try again"
    elif ch == 3:
        u=input("Passenger ID: ")
        p =input("Enter Password : ")
        passenger[u]=p
        print("ID created")
    else:
        print("Invalid login")
        return ""