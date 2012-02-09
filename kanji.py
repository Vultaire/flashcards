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

PROGRAM_NAME="Kanji"
VERSION="0.2"


class EmptyList(Exception):
    pass


class MainWindow(object):

    def __init__(self, root, data, interval, font_face, font_size, on_top):
        # GUI display
        self.root = root
        frame = Frame(root)
        frame.pack()

        font = (font_face, font_size)
        self.card = Label(frame, font=font)
        self.card.pack()

        # Card refresh interval, in seconds
        self.refresh_interval = interval

        # Data for tracking
        self.data = data
        self.pending = []
        self.current = None

        # Update card tracking
        self.reset_card()
        self.update_card()

        if on_top:
            self.root.wm_attributes("-topmost", 1)

        # Bind events
        self.root.bind("<Button-1>", self.flip_card)
        self.root.bind("<Key-Return>", self.flip_card)

    def reset_card(self):
        """
        Resets the pending list of cards.

        This method will automatically filter out duplicate entries.

        """
        self.pending = list(set(self.data[:]))

    def pull_next_card(self):
        """
        Pulls the next card from the card list.

        This method tracks the current card and will avoid pulling
        the same card two times in a row (unless there's only one
        card left to pull).

        Returns the next card.  The value is also set as
        self.current.

        """
        card = self.current
        if len(self.pending) < 1:
            raise EmptyList()
        elif len(self.pending) == 1:
            index = 0
            card = self.pending[0]
        else:
            while card == self.current:
                index = random.randint(0, len(self.pending) - 1)
                card = self.pending[index]

        del self.pending[index]

        if len(self.pending) < 1:
            self.reset_card()

        self.current = card
        self.current_index = 0
        return card

    def update_card(self):
        """
        Pulls the next card and updates the GUI.

        This is a self-recurring call.  It should only be called at
        the beginning of the application.

        """
        card = self.pull_next_card()
        self.card.configure(text=card[0])

        refresh_ms = int(self.refresh_interval * 1000)
        self.root.after(refresh_ms, self.update_card)

    def flip_card(self, event):
        self.current_index = (self.current_index + 1) % len(self.current)
        self.card.configure(text=self.current[self.current_index])


def parse_args():
    ap = argparse.ArgumentParser(
        description=_("Randomly displays characters or words in a window, "
                      "refreshing every 30 seconds or so."))
    ap.add_argument("-f", "--font-face", default=None,
        help=_("Specify font face."))
    ap.add_argument("-s", "--font-size", type=int, default=100,
        help=_("Specify font size in points.  (Default: %(default)s)"))
    ap.add_argument("-i", "--interval", type=int, default=30,
        help=_("Specify how long to wait before changing entries.  "
               "(Default: %(default)s)"))
    ap.add_argument("-t", "--on-top", action="store_true", default=False,
        help=_("Make the window stay always on top."))
    ap.add_argument("-v", "--version", action="store_true", default=False,
        help=_("Show version and exit."))
    ap.add_argument("filename",
        help=_("A UTF-8 encoded file, containing one line per character "
               "or word for review."))
    return ap.parse_args()

def main():
    import sys, csv

    options = parse_args()
    if options.version:
        print "%s v%s" % (PROGRAM_NAME, VERSION)
        sys.exit(0)

    with open(options.filename) as infile:
        reader = csv.reader(infile)
        data = [tuple([col.decode("utf-8") for col in row])
                for row in reader if len(row) > 0]

    root = Tk()
    root.title(_("Kanji"))
    window = MainWindow(root, data, options.interval, options.font_face,
        options.font_size, options.on_top)
    root.mainloop()

if __name__ == "__main__":
    main()
