#Fetches and displays details for a specific train.
def train(tname):
    if tname in traindetails:
        details = traindetails[tname]
        print("Train Name:", tname)
        print("Train Number:", details['train_no'])
        print("Route:", details["route"])
        print("Schedule:", details["schedule"])
        return " "
    else:
        return "Invalid train name"
    
def addtrain():
    trainnum=0
    route=[]
    schedule = {}
    tname = input("Enter new train name: ").lower()
    if tname in train.traindetails:
        print("Train already exists.")
        return
    else:
        trainnum = int(input("Enter train number: "))
        n=int(input("enter number of station : "))
        for i in range (0,n):
            station=input("enter station :").lower()
            route.append(station)
        print("Enter schedule times (HH:MM) for stations:")
        for j in range(len(route)):
            time = input("enter time for :"+route[j]+" ")
            schedule[route[j]] = time
    print()
    train.traindetails[tname]={'train_no': trainnum, 'route': route, 'schedule': schedule}
    train.train(tname)
    print("train added")
    
#train details
traindetails = {'varanasi express': {'train_no': 10121,'route': ['delhi', 'kanpur', 'lucknow', 'varanasi'],'schedule': {'Delhi': '07:00', 'Kanpur': '10:00', 'Lucknow': '12:00', 'Varanasi': '15:00'} },
    'mumbai express': {'train_no': 19808,'route': ['mumbai', 'surat', 'ahmedabad', 'jaipur'],'schedule': {'Mumbai': '09:00', 'Surat': '11:00', 'Ahmedabad': '14:00', 'Jaipur': '20:00'}},
    'chennai express': {'train_no': 17807,'route': ['chennai', 'pondicherry', 'vijayawada', 'visakhapatnam'],'schedule': {'Chennai': '06:00', 'Pondicherry': '08:00', 'Vijayawada': '11:30', 'Visakhapatnam': '14:30'}},
    'rajdhani': {'train_no': 12341,'route': ['shimla', 'kalka', 'chandigarh', 'ludhiana'],'schedule': {'Shimla': '07:30', 'Kalka': '09:30', 'Chandigarh': '11:00', 'Ludhiana': '13:00'}},
    'shatabdi': {'train_no': 12671,'route': ['jodhpur', 'bikaner', 'jaisalmer', 'barmer'],'schedule': {'Jodhpur': '05:00', 'Bikaner': '08:00', 'Jaisalmer': '11:00', 'Barmer': '13:30'}},
    'delhi mail':{'train_no': 11011,'route': ['delhi', 'gurgaon', 'jaipur', 'udaipur'],'schedule': {'delhi': '08:00','gurgaon': '08:30','jaipur': '11:00','udaipur': '14:00'}},
    'kolkata local': {'train_no': 11022,'route': ['kolkata', 'howrah', 'bardhaman', 'asansol'],'schedule': {'kolkata': '06:00','howrah': '06:15','bardhaman': '07:00','asansol': '08:30'}}
}