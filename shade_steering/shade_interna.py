#!/usr/bin/env python

class programme:
    def __init__(self, up_time, down_time, with_random):
        self.up_time = up_time
        self.down_time = down_time
        self.with_random = with_random

    def __repr__(self):
        return "up: %s  down: %s  with_random: %s" % (
                self.up_time, self.down_time, self.with_random)


class full_programme:
    def __init__(self, p_list):
        self.p_list = p_list  # TODO: for each day of the week

    # TODO: __repr__


class todo_rename_this:
    def __init__(self, fp_a, fp_b, mode):
        self.fp_a = fp_a
        self.fp_b = fp_b
        self.mode = mode


class mode:
    items = ["a", "b", "a b", "a rand", "b rand", "a b rand"]
    def __init__(self, start=0):
        self.start = start

    def fetch(self):
        if (start >= len(items)):
            start = 0
        result = items[start]
        start += 1
        return result


class state:
    def __init__(self, time, is_wintertime, day_of_week,
            mode):
        self.time = time
        self.is_wintertime = is_wintertime
        self.day_of_week = day_of_week
        self.mode = mode

max_count = 10
count = 0
while True:
    count += 1
    if count > max_count:
        print("Quiting after: %s attempts." % count)
        break
    print("Your choice?")
    # a = raw_input()
    a = input()
    if a not in ['h', 'j', 'k', 'l']:
        print("Please give only one of h,j,k,l")
        continue

"""
Normal mode: Show current time, shades up/down status
  Space: switch to next switch time and repeat showing
  current status

Hold <Mode> Key: toggle different modes

TODO: switch between summer/wintertime

TODO: Update programm (active programme)

TODO: Switch between prgramm a and programm b

TODO: Reset to default values (up: 08:00 down: 20:00),
  programm a active, 20:00 system time

Four keys: up,down,set and mode
  """


