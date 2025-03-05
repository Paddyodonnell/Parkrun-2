# Functions
def ms2s(time):
    try:
        parts = list(map(int, time.split(':')))  # Convert all parts to integers
        if len(parts) == 3:  # If format is H:M:S
            hours, minutes, seconds = parts
        elif len(parts) == 2:  # If format is M:S
            hours = 0
            minutes, seconds = parts
        else:
            return None  # Return 0 if the format is unexpected

        return (hours * 3600) + (minutes * 60) + seconds
    except (ValueError, AttributeError):
        return None

def s2ms(seconds):
    minutes = int(seconds//60)
    seconds = int(seconds%60)
    if seconds < 10:
        seconds = f'0{seconds}'
    return f'{minutes}:{seconds}'