import pyautogui
import time
import keyboard
from PIL import ImageGrab

# Disable the fail-safe feature
pyautogui.FAILSAFE = False

# Default settings for color checking and cursor locking
SHOULD_CHECK_COLOR = False
SHOULD_LOCK_CURSOR = False

# List of RGB color values that are considered acceptable
# These colors are used in the is_color_green function to check if a pixel color is within the acceptable range
ACCEPTABLE_COLORS = [
    (139, 183, 61), (138, 183, 60), (133, 176, 58), (134, 179, 59),
    (136, 179, 59), (140, 185, 61), (141, 186, 60), (140, 185, 61),
    (141, 186, 61), (139, 185, 61), (137, 181, 59), (131, 176, 58),
    (141, 186, 61), (138, 183, 60), (137, 181, 60), (137, 182, 60),
    (131, 176, 58), (127, 171, 55), (134, 178, 59), (141, 186, 61),
    (136, 179, 59), (134, 179, 58), (137, 182, 60), (141, 186, 61),
    (133, 176, 58), (140, 185, 60), (141, 186, 60), (140, 185, 61),
    (139, 184, 61), (141, 186, 61)
]

# Function to simulate a left mouse click at the current mouse position
def click_left_mouse():
    # Use the pyautogui library to click the left mouse button
    pyautogui.click()

# Function to move the mouse to the specified (x, y) coordinates
def move_mouse_to_coordinates(x, y):
    # Use the pyautogui library to move the mouse to the specified coordinates
    pyautogui.moveTo(x, y, duration=0)


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


# Function to check if a given pixel color is within the acceptable range
def is_color_green(pixel_color, tolerance=30):
    # For each color in the list of acceptable colors
    # Check if the absolute difference between each RGB component of the pixel color and the acceptable color is within the tolerance
    # If any color in the list satisfies this condition, return True
    return any(
        all(abs(pixel_color[i] - color[i]) <= tolerance for i in range(3))
        for color in ACCEPTABLE_COLORS
    )


# Function to check if a specific color is present in the area around the cursor
def is_color_in_area_around_cursor(cursor_x, cursor_y, width, height):
    # Calculate the coordinates for the screenshot area around the cursor
    x = max(cursor_x - width // 2, 0)
    y = max(cursor_y - height // 2, 0)

    # Take a screenshot of the area around the cursor
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # For each pixel in the screenshot
    for px in range(width):
        for py in range(height):
            # Get the color of the pixel
            pixel_color = screenshot.getpixel((px, py))

            # If the pixel color is green, print 'true' and return True
            if is_color_green(pixel_color):
                print('true')
                return True
            
    # If no green pixel was found, return False
    return False

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
    cursor_x, cursor_y = pyautogui.position()

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
