XvfbRobot library for Robot Framework
==================================================


Introduction
------------

A simple robot library for creating virtual display which can be used for running selenium tests in headless mode, internally uses a [xvfbwrapper](https://pypi.python.org/pypi/xvfbwrapper/0.2.5).

- Information about keywords can be found on the [Keyword Documentation](https://github.com/drobota/robotframework-xvfb/docs/robotframework-xvfb.html) page.


Requirements
------------
* Python 2.7.10
* Python 3.4
* Python 3.5
* Robot Framework 2.8 
* xvfbwrapper (python library)

Installation
------------
#### Using pip ####

The recommended installation tool is [pip](http://pip-installer.org).

Install pip.
Enter the following:

    pip install robotframework-xvfb
    
Usage
------------

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      Selenium2Library
    Library      XvfbRobot
    *** Test Cases ***
    Create Headless Browser
        Start Virtual Display    1920    1080
        Open Browser   http://google.com
        Set Window Size    1920    1080
        ${title}=    Get Title
        Should Be Equal    Google    {title}
        [Teardown]    Close Browser
        
Getting Help
------------
The [user group for Robot Framework](http://groups.google.com/group/robotframework-users) is the best place to get help. Include in the post:

- Full description of what you are trying to do and expected outcome
- Version number of robotframework-xvfb, Robot Framework and xvfbwrapper
- Traceback or other debug output containing error information

Or create an issue on [github](https://github.com/drobota/robotframework-xvfb)