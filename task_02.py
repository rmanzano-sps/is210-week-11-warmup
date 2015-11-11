#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a class from the ground up"""

import time

class Snapshot:
    """This clas holds a constructor for snapshot, its instance\
attribute holds the unix time stamp"""
    def __init__(self):
        self.created = time.time()
