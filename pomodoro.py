#!/usr/bin/env python3

"""Pomodoro CLI program

Usage examples:

$ pomodoro.py p  # start a pomodoro timer
$ pomodoro.py s  # start a short break timer

"""

import sys
import time


POMODORO_LENGTH = 25 * 60  # pomodoro length in seconds
SHORT_BREAK_LENGTH = 5 * 60  # short break length in seconds


class Session:
    """superclass for sessions"""

    def __init__(self, counter=60):
        self.counter = counter
        self.name = "Session"

    def run(self):
        """run()"""
        print(self.name)
        while self.counter > 0:
            minutes = int(self.counter / 60)
            seconds = self.counter - minutes * 60
            print("   {:02d}:{:02d}".format(minutes, seconds), end="\r")
            time.sleep(1)
            self.counter -= 1


class Pomodoro(Session):
    """pomodoro session class"""
    def __init__(self, counter=POMODORO_LENGTH):
        self.counter = counter
        self.name = "Pomodoro"


class ShortBreak(Session):
    """short break session class"""
    def __init__(self, counter=SHORT_BREAK_LENGTH):
        self.counter = counter
        self.name = "Short break"


def main():
    """main"""
    if len(sys.argv) == 1:
        print(__doc__)
    elif len(sys.argv) == 2:
        cmd = sys.argv[1]
        if cmd == "p":
            session = Pomodoro()
        elif cmd == "s":
            session = ShortBreak()
        session.run()


if __name__ == "__main__":
    main()

