# function to convert time to 24 hrs

def convert(hour , minute , period):
    if period == "AM" and hour in range(0, 13):
        time = (f"{(hour-0)}{minute}hrs")
        return time
    elif (period == "PM" and hour in range(0,13)):
        times = (f"{(hour+12)}{minute}hrs")
        return times
    else:
        return ("Invalid time")
converted= convert(10 , 30 , "AM")
print (converted)