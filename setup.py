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

import sys
from distutils.core import setup
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "XvfbRobot"))

exec(compile(open(join(dirname(__file__), "XvfbRobot", "version.py")).read(), 'version.py', 'exec'))


setup(name              = "robotframework-xvfb",
      version           = VERSION,
      description       = "Robot library for interacting with Xvfb",
      long_description  = "XvfbRobot is a robot library which is a wrapper for a xvfbwrapper",
      author            = "Dmitriy Robota",
      author_email      = "dmitriy.robota@gmail.com",
      url               = "https://github.com/drobota/robotframework-xvfb",
      license           = "Apache License 2.0",
      keywords          = "robotframework robot testing testautomation xvfb xvfbwrapper xvfbrobot",
      platforms         = "Unix",
      classifiers       = [   "License :: OSI Approved :: Apache Software License",
                              "Programming Language :: Python",
                              "Operating System :: POSIX :: Linux",
                              "Operating System :: Unix",
                              "Programming Language :: Python :: 2.7",
                              "Programming Language :: Python :: 3.4",
                              "Programming Language :: Python :: 3.5",
                              "Topic :: Software Development :: Testing",
                              "Topic :: Software Development :: Quality Assurance",
                              "Framework :: Robot Framework"
                        ],
      install_requires  = ["robotframework","xvfbwrapper"],
      packages          = ["XvfbRobot"],
      download_url      = "https://github.com/drobota/robotframework-xvfb",
      )
