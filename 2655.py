import time

def focus_timer_task():
    print("Stay focused! Task executed.")

if __name__ == "__main__":
    try:
        while True:
            focus_timer_task()
            time.sleep(1200)

    except KeyboardInterrupt:
        print("\nFocus timer interrupted. Exiting.")
