=======
 Kanji
=======
A simple study program for students of Japanese
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a quick application I coded in Python/Tkinter.  It is meant to
load a list of characters or words and display them one-by-one,
refreshing every 30 seconds or so.

On Windows, this application runs in an "always-on-top" mode.  I plan
to add a toggle menu later.  Linux WMs generally have a toggle on each
window already, so if you're running Linux, setting always-on-top is
up to you.

This is a *dirt simple* application; it's intentionally minimalistic
and I plan to keep it this way.  However, I may add a few minimal
options later, such as font selection and adjustable refresh interval.

Syntax::

  kanji.py <utf-8 encoded data file>

The data file should have one entry per line.  Lines are not limited
to single characters, in case you wish to study words or something
other than Kanji.

**Note:** currently if no file is provided, a dummy data list is used
instead.
