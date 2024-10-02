import pygetwindow as gw
import keyboard
import time

# Specify the title of the window you want to focus
WINDOW_TITLE = "hi"

def window_exists():
    """Check if the window with the specified title exists."""
    return any(WINDOW_TITLE in window.title for window in gw.getAllWindows())

def focus_window():
    if window_exists():
        window = gw.getWindowsWithTitle(WINDOW_TITLE)[0]
        window.activate()  # Focus the window
    else:
        print(f"No window found with title: {WINDOW_TITLE}")

def main():
    print("Press 'p' to exit the script.")
    while True:
        focus_window()
        time.sleep(1)  # Focus the window every second

        if keyboard.is_pressed('p'):
            print("Exiting script.")
            break

if __name__ == "__main__":
    main()
