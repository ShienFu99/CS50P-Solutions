#Description: Prompts the user for a time -> Determines if it's breakfast time, lunch time or dinner time
#Completed optional challenge -> Supports a.m. and p.m.
def main():
    time_str = input("What time is it? ")
    time = convert(time_str)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    #minutes_unfixed might contain a.m. or p.m.
    hours, minutes_unfixed = time.split(":", 1)

    #if minutes_unfixed contains a.m. or p.m. -> keeps track of it, then removes it from minutes (30 a.m. -> 30 [minutes])
    if minutes_unfixed.find("a.m.") != -1:
        minutes, discard = minutes_unfixed.split(" ", 1)
        hour_period = "a.m."
    elif minutes_unfixed.find("p.m.") != -1:
        minutes, discard = minutes_unfixed.split(" ", 1)
        hour_period = "p.m."
    else:
        minutes = minutes_unfixed
        hour_period = None

    hours, minutes = float(hours), float(minutes)

    #Returns the time to main() as a float value
    match hour_period:
        case "a.m." | None:
            return round(hours + minutes / 60, 1)
        case "p.m.":
            return round((hours + 12) + minutes / 60, 1)

main()
