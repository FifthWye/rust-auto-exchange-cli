import pyautogui
from PIL import ImageGrab

# Disable the fail-safe feature
pyautogui.FAILSAFE = False


# Function to move the mouse to the specified (x, y) coordinates
def move_mouse_to_coordinates(x, y):
    # Use the pyautogui library to move the mouse to the specified coordinates
    pyautogui.moveTo(x, y, duration=0)


# Function to simulate a left mouse click at the current mouse position
def click_left_mouse():
    # Use the pyautogui library to click the left mouse button
    pyautogui.click()


def get_mouse_position():
    # Get the current mouse position using pyautogui
    cursor_x, cursor_y = pyautogui.position()
    return cursor_x, cursor_y

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
