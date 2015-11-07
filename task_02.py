#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_02
Creating a class

"""
import time


class Snapshot(object):
    """
    Stores a Unix timestamp

    Args:
        None

    Attributes:
        created (Time): Unix timestamp
    """
    def __init__(self):
        self.created = time.time()