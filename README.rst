=======
 Kanji
=======
A simple study program for students of Japanese
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: Paul Goins
:License: GNU General Public License, Version 2 or Later

Summary
=======

This is a quick application I coded in Python/Tkinter.  It is meant to
load a list of characters or words and display them one-by-one,
refreshing every 30 seconds or so.  The window can be set as
always-on-top, allowing you to passively study while working on other
tasks.

All options are configurable via the command line.  This is
intentional: I don't want a lot of GUI code in this application, and
I'd like to keep usage of screen real estate to a minimum.

A nice side effect of writing it this way: it should be easy to call
this program from within another tool or study program, for those so
inclined.

Requirements
============

- Windows: Python 2.7.  See note below.
- Linux users: Python 2.7 with Tkinter, or Python 2.6 with Tkinter and argparse

**Note:** This tool **must** have its arguments supplied via the
command line, or via a wrapper script; there are no interactive
GUI-based dialogs for telling the program what to do.

Help
====

::

  usage: kanji.py [-h] [-f FONT_FACE] [-s FONT_SIZE] [-i INTERVAL] [-t] [-v]
                  filename
  
  Randomly displays characters or words in a window, refreshing every 30 seconds
  or so.
  
  positional arguments:
    filename              A UTF-8 encoded file, containing one line per
                          character or word for review.
  
  optional arguments:
    -h, --help            show this help message and exit
    -f FONT_FACE, --font-face FONT_FACE
                          Specify font face.
    -s FONT_SIZE, --font-size FONT_SIZE
                          Specify font size in points. (Default: 100)
    -i INTERVAL, --interval INTERVAL
                          Specify how long to wait before changing entries.
                          (Default: 30)
    -t, --on-top          Make the window stay always on top.
    -v, --version         Show version and exit.
