=============
 Flash Cards
=============
A simple flash card program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: Paul Goins
:License: GNU General Public License, Version 2 or Later

**Note:** this project was formerly known as "Kanji", but has been
renamed to reflect its now more general target audience.

Summary
=======

This is a quick application I coded in Python/Tkinter.  It is meant to
load a list of characters or words and display them one-by-one,
refreshing every 30 seconds or so.  The window can be set as
always-on-top, allowing you to passively study while working on other
tasks.

"Flippable" cards can be created by writing the word list as a CSV
file.  Each card is represented by one CSV line, containing one or
more comma-separated values.  To flip, just click the window to go to
the next value for the card.  `1`_

All options are configurable via the command line.  This is
intentional: I don't want a lot of GUI code in this application, and
I'd like to keep usage of screen real estate to a minimum.

A nice side effect of writing it this way: it should be easy to call
this program from within another tool or study program, for those so
inclined.

Requirements
============

You must have Python 2.7 with Tkinter, or Python 2.6 with Tkinter and
argparse.  The program has been tested on both Windows and Linux.

**Note:** This tool **must** have its arguments supplied via the
command line, or via a wrapper script; there are no interactive
GUI-based dialogs for telling the program what to do.

Help
====

Usage
-----

::

  usage: flashcards.py [-h] [-f FONT_FACE] [-s FONT_SIZE] [-i INTERVAL] [-t]
                       [-v]
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

In-program keybindings
----------------------

| Enter, space bar or left click: **flip forward**
| Backspace or right click: **flip backward**

Footnotes
=========

.. [1] For advanced users, Excel-style CSV formatting is used, so it
   is possible to include quotation marks or commas in a value.
   double-quotes are used for both escaping and quoting values.
