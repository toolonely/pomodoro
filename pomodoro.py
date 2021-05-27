#!/usr/bin/env python3

"""Pomodoro CLI program

Usage examples:

$ pomodoro.py  # start a pomodoro timer

"""

import time


POMODORO_LENGTH = 25 * 60  # pomodoro length in seconds


class Pomodoro:
    """pomodoro session class"""
    def run(self):
        """run()"""
        print("Pomodoro")
        counter = POMODORO_LENGTH
        while counter > 0:
            minutes = int(counter / 60)
            seconds = counter - minutes * 60
            print("   {:02d}:{:02d}".format(minutes, seconds), end="\r")
            time.sleep(1)
            counter -= 1


def main():
    """main"""
    pomodoro = Pomodoro()
    pomodoro.run()


if __name__ == "__main__":
    main()

