# function to convert time to 24 hrs

def convert(hour , minute , period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}{minute:02d}"
converted= convert(12 , 10 , "pm")
print (converted)