# rust-auto-exchange-cli

This script contains a set of functions to automate mouse movements and clicks using the `pyautogui` library. It also uses the `keyboard` library to listen for key presses and the `PIL` library to capture screenshots.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/FifthWye/rust-auto-exchange-cli.git
```

2. Navigate to the project directory:

```bash
cd rust-auto-exchange-cli
```

3.Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python main.py
```

This will start the script with the default parameters. If you want to enable color checking and cursor locking, you can modify the exchange function call in main.py as follows:

```python
exchange(should_check_color=True, should_lock_cursor=True)
```

To stop the script, simply press the `\` key.

## Functions

- `click_left_mouse()`: Simulates a left mouse click at the current mouse position.
- `move_mouse_to_amount_input()`: Moves the mouse to a specific position on the screen.
- `move_mouse_to_coordinates(x, y)`: Moves the mouse to the specified (x, y) coordinates.
- `exit_loop(e)`: Listens for a specific key press to toggle a flag that controls the execution of a loop.

## Key Controls

The script uses several keys to control its behavior:

1. `\` key: The script listens for the `\` key press to exit the loop. When the `\` key is pressed, the `exit_loop` function is called, which sets the `exit_flag` to `True`, causing the `while` loop in the `exchange` function to terminate.

## Parameters

1. `should_check_color`: This is a boolean flag that determines whether the script should check for a specific color in the area around the cursor. If this flag is set to `True`, the script will call the `is_color_green` function to check if any pixel in the specified area matches the acceptable colors. This can be useful if you want the script to perform certain actions only when a specific color is present on the screen.

2. `should_lock_cursor`: This is another boolean flag that controls whether the cursor should be locked to a specific position. If this flag is set to `True`, the script will move the cursor back to its original position every 10 iterations. This can be useful if you want to prevent the cursor from drifting away from a specific area on the screen.

## Running Tests

This project uses Python's built-in `unittest` module for testing.

To run the tests, follow these steps:

1. Open a terminal.

2. Navigate to the project directory.

3. Run the tests with the `python -m unittest` command followed by the name of the test file without the `.py` extension. For example:
