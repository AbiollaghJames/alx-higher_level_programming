#!/usr/bin/python3
""" a class LockedClass with no class or object attribute
"""


class LockedClass:
    """__slots__ conserve memoery and prevent creating
      objects on runtime
      """
    __slots__ = ["first_name"]
