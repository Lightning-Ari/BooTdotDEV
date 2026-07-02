"""import curses
from curses import wrapper
import curses.ascii 

def main(stdscr):
    stdscr.clear()
    while True:
        # Fetch current bounds
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"Current Window Size: {height}x{width} (Press Ctrl + x to quit)")
        stdscr.refresh()
        
        # Get character input
        key = stdscr.getch()
        
        # ASCII value 17 represents Ctrl+Q (or use curses.ascii.DC1)
        if key == curses.ascii.ctrl(ord('x')):
            break
        elif key == curses.KEY_RESIZE:
            # Clear old positions to clean up fragments after window changes size
            stdscr.clear() 
            # In some environments, calling curses.resizeterm(0, 0) forces an adjustment
            curses.resizeterm(0, 0)

wrapper(main)
"""

import curses
import datetime
import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Get current day and time in UTC format (yyyy-mm-dd)
    today = "2026-06-11"

    # Convert local time to UTC using 0001 as time offset for timezone-aware dates
    user_local_time_stringUTCFormatted = f"{today} + {datetime UTC+05:30:00}"

    display_timestamp = f"Today: {today}, Local Time: {user_local_time_stringUTCFormatted}"

    stdscr.addstr(2, 12, "\n" + display_timestamp)
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == ord('\n'):
            # Convert user's stated local time to UTC using Python's datetime.strptime function
            user localtime_strUTCFormatted = input("Enter your local time (HH:MM): ")

            # Parse user's local time string into a timestamp in UTC format
            try:
                local_time = datetime.strptime(user_local_time_strUTCFormatted, "%H:%M")
            except ValueError:
                print("Invalid date or time format. Please enter an hour and minute.")
                continue

            # Get the current UTC time and convert to local time (adjusting for timezone)
            userlocal_time_string = input("Enter your current local time in UTC: ")
            try:
                now_localtime = datetime.strptime(userlocal_time_string, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date or time format. Please enter an hour and minute.")
                continue

            user_utc_offset = int(user localtime_strUTCFormatted.split(':')[0]) * 3600
            now_utc = datetime.utcnow() - datetime.utcfromtimestamp(now_localtime.timestamp())

            # Get the current day in UTC
            today = datetime.utcfromtimestamp(now_utc.timestamp())

            # Update display with current local time and user/local time information
            display_timestamp = f"Today: {today}, Local Time: {format(userlocal_time_string, '%Y-%m-%d %H:%M')}"

    return 0

# Start the application
curses.wrapper(main)