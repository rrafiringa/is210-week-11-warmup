#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_04
Subclassing.
"""

import car


class CustomCar(car.Car):
    """
    Custom four wheeled vehicle
    Args:
        color (String): Vehicle color
        tires (List): List of CustomTire objects
    Attributes:
        color (String): Color attribute inherited from superclass car.Car
        tires (List): Tires on the vehicle
    """
    def __init__(self, color='Red', tires=None):
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = [CustomTire() for i in range(4) if isinstance(i, int)]


class CustomTire(car.Tire):
    """ Custom rolling support for a vehicle """
    __maximum_miles = 500