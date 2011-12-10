=======
 Kanji
=======
A simple study program for students of Japanese
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a quick application I coded in Python/Tkinter.  It is meant to
load a list of characters or words and display them one-by-one,
refreshing every 30 seconds or so.

Ideally this application should be used in an "always-on-top" mode, so
you can passively look at the window while working on other things. `1`_

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

.. [1] No "always-on-top" support is currently built-in, although I
       may add Windows-specific support in the future.  (This isn't
       necessary on Linux.)
