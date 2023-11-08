import time
import keyboard
from utils import *

# Default settings for color checking and cursor locking
SHOULD_CHECK_COLOR = False
SHOULD_LOCK_CURSOR = False

# Function to handle the '\' key press event
def exit_loop(e):
    # When the '\' key is pressed, set the global exit_flag to True
    global exit_flag
    # Invert the value of exit_flag
    exit_flag = not exit_flag
    if exit_flag:
        print("Loop paused.")
    else:
        print("Loop resumed.")


# Set a listener for the '\' key press to call the exit_loop function
keyboard.on_press_key('\\', exit_loop)

# Global flag to control the execution of the loop
exit_flag = False


# Main function to automate mouse movements and clicks
def exchange(should_check_color, should_lock_cursor):
    # Counter for the number of iterations
    iteration_count = 0

    # Wait for 5 seconds before starting the loop
    time.sleep(5)

    # Get the current mouse position
    cursor_x, cursor_y = get_mouse_position()

    # Main loop
    while not exit_flag:
        # If cursor locking is enabled and the current iteration is a multiple of 10
        if should_lock_cursor or should_check_color and iteration_count % 10 == 0:
            # Move the mouse back to its original position
            move_mouse_to_coordinates(cursor_x, cursor_y)

        # Increment the iteration counter
        iteration_count += 1

        # Rest the counter after 10 iterations
        if iteration_count >= 10:
            iteration_count = 0

        # If color checking is enabled and the color around the cursor matches the acceptable colors
        if should_check_color and is_color_in_area_around_cursor(cursor_x, cursor_y, 10, 10):
            # Click the left mouse button
            click_left_mouse()
        else:
            # If color checking is disabled
            if should_check_color == False:
                # Click the left mouse button
                click_left_mouse()


while True:
    if not exit_flag:
        print("Starting...")
        exchange(SHOULD_CHECK_COLOR, SHOULD_LOCK_CURSOR)
    else:
        time.sleep(1)
