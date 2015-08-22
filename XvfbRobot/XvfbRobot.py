#!/usr/bin/env python

#  Copyright 2015 Dmitriy Robota.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import atexit
from xvfbwrapper import Xvfb
from robot.api import logger


class XvfbRobot:
    _display = None

    def start_virtual_display(self, width=1440, height=900,
                              color_depth=24, **kwargs):
        """Starts virtual display which will be
         destroyed after test execution will be end

        *Arguments:*
        - width: a width to be set in pixels
        - height: a height to be set in pixels
        - color_depth: a color depth to be used
        - kwargs: extra parameters

        *Example:*

        | Start Virtual Display |
        | Start Virtual Display | 1920 | 1080 |
        | Start Virtual Display | ${1920} | ${1080} | ${16} |
        """
        if self._display is None:
            logger.info("Using virtual display: '{0}x{1}x{2}'".format(
                        width, height, color_depth))
            self._display = Xvfb(int(width), int(height),
                                 int(color_depth), **kwargs)
            self._display.start()
            atexit.register(self._display.stop)
