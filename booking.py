# Handles the logic for booking tickets, including validating stations and checking route direction.
def book(tname, traindetails, start, end, seat):
    if tname not in traindetails:
        return "Train not found."

    train = traindetails[tname]
    route = train['route']
    if start not in route or end not in route:
        return "Invalid stations entered."

    start_index = route.index(start)
    end_index = route.index(end)

    if start_index >= end_index:
        return "End station must come after start station on the route."
    print("Successfully booked" ,seat,"seat on " ,tname, " from" ,start ," to" ,end)
    return ""