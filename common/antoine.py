"""
Common module to approximate vapor pressures based on the antoine equation
"""

from typing import Optional
import math


class AntoineComponent:
    def __init__(self, name, A, B, C, p_unit="Pa", base="log10"):
        self.name = name
        self.A = A
        self.B = B
        self.C = C
        self.p_unit = p_unit  # 'mmHg', 'bar', 'Pa', 'kPa'
        self.base = base  # 'log10' or 'ln'

    def get_vapor_pressure(self, T: float) -> float:  # Unit: Pa
        exponent = self.A - self.B / (self.C - T)

        if self.base == "log10":
            p_raw = 10**exponent
        elif self.base == "ln":
            p_raw = math.exp(exponent)
        else:
            raise ValueError(f"Unknown base: {self.base}")

        if self.p_unit.lower() == "mmhg":
            return p_raw * 133.322368
        elif self.p_unit.lower() == "bar":
            return p_raw * 100000.0
        elif self.p_unit.lower() == "kpa":
            return p_raw * 1000.0
        elif self.p_unit.lower() == "pßa":
            return p_raw
        else:
            raise ValueError(f"Unknown unit for pressure: {self.p_unit}")
