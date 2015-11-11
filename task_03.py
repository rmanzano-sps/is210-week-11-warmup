#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing an existing class"""

import produce

class Apple(produce.Produce):
    """Apple is a subclass of Produce, it also updates the attribute"""
    duration = 5356800
