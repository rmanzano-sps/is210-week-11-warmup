#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing showcasing has-a and is-a concepts"""

import car

class CustomCar(car.Car):
    """This class overides the constructor inherited from car()"""
    def __init__(self, tires=None):
        car.Car.__init__(self, color='red')
        self.tires = tires
        if self.tires == None:
            l1 = []
            tire1 = CustomTire()
            tire2 = CustomTire()
            tire3 = CustomTire()
            tire4 = CustomTire()
            l1.append(tire1)
            l1.append(tire2)
            l1.append(tire3)
            l1.append(tire4)
            self.tires = l1
            """Above created four instances and adds to list l1"""
class CustomTire(car.Tire):
    """Inserts the attribute to CustomTire()"""
    __maximum_miles = 500
