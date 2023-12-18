import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Use '\r' to overwrite the display on the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    focus_minutes = int(input("Enter the focus minutes: "))
    focus_timer(focus_minutes)
