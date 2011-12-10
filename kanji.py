#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Label
import os, gettext, random
gettext.install("net.vultaire.kanji")


class EmptyList(Exception):
    pass


class MainWindow(object):

    def __init__(self, root, data, interval=30):
        # GUI display
        self.root = root
        frame = Frame(root)
        frame.pack()

        self.kanji = Label(frame, font=(None,100))
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


def main():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as infile:
            data = infile.read()
        data = [s.decode("utf-8") for s in data.splitlines()]
    else:
        test_data = [
            u"鯨",
            u"食事",
            u"勉強",
            u"春夏秋冬",
            u"甘",
            ]
        data = test_data

    root = Tk()
    root.title(_("Kanji"))
    window = MainWindow(root, data, interval=30)
    root.mainloop()

if __name__ == "__main__":
    main()
