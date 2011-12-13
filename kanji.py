#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Kanji

Author: Paul Goins <general@vultaire.net>
License: GNU GPL v2 or later

"""

from Tkinter import Tk, Frame, Label
import argparse, os, gettext, random
gettext.install("net.vultaire.kanji")


class EmptyList(Exception):
    pass


class MainWindow(object):

    def __init__(self, root, data, interval, font_face, font_size):
        # GUI display
        self.root = root
        frame = Frame(root)
        frame.pack()

        font = (font_face, font_size)
        self.kanji = Label(frame, font=font)
        self.kanji.pack()

        # Kanji refresh interval, in seconds
        self.refresh_interval = interval

        # Data for tracking
        self.data = data
        self.pending = []
        self.current = None

        # Update kanji tracking
        self.reset_kanji()
        self.update_kanji()

        # Windows-only: set always-on-top
        if os.name == "nt":
            self.set_always_on_top()

    def reset_kanji(self):
        """
        Resets the pending list of kanji.

        This method will automatically filter out duplicate entries.

        """
        self.pending = list(set(self.data[:]))

    def pull_next_kanji(self):
        """
        Pulls the next kanji from the kanji list.

        This method tracks the current kanji and will avoid pulling
        the same kanji two times in a row (unless there's only one
        kanji left to pull).

        Returns the next kanji.  The value is also set as
        self.current.

        """
        kanji = self.current
        if len(self.pending) < 1:
            raise EmptyList()
        elif len(self.pending) == 1:
            index = 0
            kanji = self.pending[0]
        else:
            while kanji == self.current:
                index = random.randint(0, len(self.pending) - 1)
                kanji = self.pending[index]

        del self.pending[index]

        if len(self.pending) < 1:
            self.reset_kanji()

        self.current = kanji
        return kanji

    def update_kanji(self):
        """
        Pulls the next kanji and updates the GUI.

        This is a self-recurring call.  It should only be called at
        the beginning of the application.

        """
        kanji = self.pull_next_kanji()
        self.kanji.configure(text=kanji)

        refresh_ms = int(self.refresh_interval * 1000)
        self.root.after(refresh_ms, self.update_kanji)

    def set_always_on_top(self):
        self.root.wm_attributes("-topmost", 1)


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--font-face", default=None,
        help=_("Specify font face."))
    ap.add_argument("-s", "--font-size", type=int, default=100,
        help=_("Specify font size in points.  (Default: %(default)s)"))
    ap.add_argument("-i", "--interval", type=int, default=30,
        help=_("Specify how long to wait before changing entries.  "
               "(Default: %(default)s)"))
    ap.add_argument("filename",
        help=_("A UTF-8 encoded file, containing one line per character "
               "or word for review."))
    return ap.parse_args()

def main():
    import sys

    options = parse_args()

    with open(options.filename) as infile:
        data = infile.read()
        data = [s.decode("utf-8") for s in data.splitlines()]

    root = Tk()
    root.title(_("Kanji"))
    window = MainWindow(root, data, options.interval, options.font_face,
        options.font_size)
    root.mainloop()

if __name__ == "__main__":
    main()
