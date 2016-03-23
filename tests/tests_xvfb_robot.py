import os
import unittest

from XvfbRobot import XvfbRobot


def reset_display():
    os.environ["DISPLAY"] = ":0"


class TestXvfbRobot(unittest.TestCase):

    def setUp(self):
        reset_display()

    def test_start_virtual_display(self):
        xvfb_robot = XvfbRobot()
        xvfb_robot.start_virtual_display()
        display_var = ':{0}'.format(xvfb_robot._display.new_display)
        self.assertIsNotNone(xvfb_robot._display)
        self.assertEqual(display_var, os.environ['DISPLAY'])

    def test_start_without_existing_display(self):
        del os.environ['DISPLAY']
        xvfb_robot = XvfbRobot()
        xvfb_robot.start_virtual_display()
        display_var = ':{0}'.format(xvfb_robot._display.new_display)
        self.assertIsNotNone(xvfb_robot._display)
        self.assertEqual(display_var, os.environ['DISPLAY'])

    def test_start_with_kwargs(self):
        w = 800
        h = 600
        depth = 16
        xvfb_robot = XvfbRobot()
        xvfb_robot.start_virtual_display(width=w, height=h, colordepth=depth)
        self.assertIsNotNone(xvfb_robot._display)
        self.assertEqual(w, xvfb_robot._display.width)
        self.assertEqual(h, xvfb_robot._display.height)
        self.assertEqual(depth, xvfb_robot._display.colordepth)
        display_var = ':{}'.format(xvfb_robot._display.new_display)
        self.assertEqual(display_var, os.environ['DISPLAY'])

    def test_start_with_arbitrary_kwargs(self):
        xvfb_robot = XvfbRobot()
        xvfb_robot.start_virtual_display(nolisten="tcp")
        self.assertIsNotNone(xvfb_robot._display)
        display_var = ':{}'.format(xvfb_robot._display.new_display)
        self.assertEqual(display_var, os.environ['DISPLAY'])

    def test_start_fails_with_unknown_kwargs(self):
        xvfb_robot = XvfbRobot()
        with self.assertRaises(RuntimeError):
            xvfb_robot.start_virtual_display(foo="bar")
