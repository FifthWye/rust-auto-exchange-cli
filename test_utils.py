import unittest
import mock  # Python 2
import utils
import pyautogui
from PIL import Image


class TestUtils(unittest.TestCase):
    def test_is_color_green(self):
        # Test that the function correctly identifies a green color
        self.assertTrue(utils.is_color_green((139, 183, 61)))
        # Test that the function correctly identifies a non-green color
        self.assertFalse(utils.is_color_green((255, 255, 255)))

    def test_is_color_in_area_around_cursor(self):
        # Mock the ImageGrab.grab function to return a green image
        utils.ImageGrab.grab = mock.Mock(
            return_value=Image.new('RGB', (200, 200), (139, 183, 61)))
        # Test that the function correctly identifies a green area
        self.assertTrue(
            utils.is_color_in_area_around_cursor(100, 100, 200, 200))
        # Mock the ImageGrab.grab function to return a non-green image
        utils.ImageGrab.grab = mock.Mock(
            return_value=Image.new('RGB', (200, 200), (255, 255, 255)))
        # Test that the function correctly identifies a non-green area
        self.assertFalse(
            utils.is_color_in_area_around_cursor(100, 100, 200, 200))

    def test_move_mouse_to_coordinates(self):
        # Mock the pyautogui.moveTo function to check if it's called with the correct arguments
        pyautogui.moveTo = mock.Mock()
        utils.move_mouse_to_coordinates(100, 200)
        pyautogui.moveTo.assert_called_once_with(100, 200, duration=0)

    def test_click_left_mouse(self):
        # Mock the pyautogui.click function to check if it's called
        pyautogui.click = mock.Mock()
        utils.click_left_mouse()
        pyautogui.click.assert_called_once()

    def test_get_mouse_position(self):
        # Mock the pyautogui.position function to return a specific position
        pyautogui.position = mock.Mock(return_value=(100, 200))
        cursor_x, cursor_y = utils.get_mouse_position()
        self.assertEqual(cursor_x, 100)
        self.assertEqual(cursor_y, 200)


if __name__ == '__main__':
    unittest.main()
