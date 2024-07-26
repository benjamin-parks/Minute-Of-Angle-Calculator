yards = int(input("How many yards are you shooting at? "))

def calculate_drop(yards):
    drop = {
        25: -1,
        50: 0.5,
        100: 0,
        200: -4,
        300: -15,
        400: -32,
        500: -60,
    }
    
    for key in drop:
        if yards == key:
            return drop[key] if drop[key] > 0 else abs(drop[key])
    else:
        return "Invalid distance"


def moa(yards):
    if yards == 25: # at 25 yards, we are 1 inch low (1 inch * 4 to get to 100 yards = 4moa)
        return 4
    elif yards == 50: # at 50 yards, we are .5 inch low (.5 inch * 2 to get to 100 yards = 1moa)
        return 1
    elif yards % 100 == 0:
        return yards / 100
    else:
        return "Invalid distance"



def calculate_adjustment(yards):
    drop = calculate_drop(yards)
    min_of_angle = moa(yards)
    if min_of_angle == "Invalid distance":
        return "Invalid distance entered. Try again with either 25, 50, 100, 200, 300, 400, or 500"
    elif min_of_angle < 0:
        return f"You need to come up {min_of_angle} MOA"
    return f"You need to come up {drop / min_of_angle} MOA"

# calculate adjustment for drop


print(calculate_adjustment(yards))
