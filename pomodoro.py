#!/usr/bin/env python3

"""Pomodoro CLI program

Usage examples:

$ pomodoro.py  # start a pomodoro timer

"""

import time


POMODORO_LENGTH = 25 * 60  # pomodoro length in seconds


class Pomodoro:
    """pomodoro session class"""
    def __init__(self, counter=POMODORO_LENGTH):
        self.counter = counter

    def run(self):
        """run()"""
        print("Pomodoro")
        while self.counter > 0:
            minutes = int(self.counter / 60)
            seconds = self.counter - minutes * 60
            print("   {:02d}:{:02d}".format(minutes, seconds), end="\r")
            time.sleep(1)
            self.counter -= 1


def main():
    """main"""
    pomodoro = Pomodoro()
    pomodoro.run()


if __name__ == "__main__":
    main()

