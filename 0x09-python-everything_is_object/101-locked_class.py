#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for anything but attributes called 'last_name'.
    """
    __slots__ = ["last_name"]
