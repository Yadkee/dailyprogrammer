#! python3
# -*- coding: utf-8 -*-
"""Only implemented sum, multiplication and inversion.
Made use of classes and operator override."""
from random import random


class Number():
    precision = 16

    def __init__(self, param):
        if isinstance(param, Number):
            self.stream = param.stream
        elif isinstance(param, str):
            self.stream = param
        elif isinstance(param, float):
            self.stream = "".join("0" if random() > param else "1"
                                  for _ in range(self.precision))
        self.ln = len(self.stream)

    @property
    def value(self):
        return self.stream.count("1") / len(self.stream)

    def __str__(self):
        return "%s... (%f)" % (self.stream[:16], self.value)

    def __invert__(self):
        return Number("".join("0" if i == "1" else "1" for i in self.stream))

    def __add__(self, other):  # (self + other / 2)
        other = Number(other)
        assert self.ln == other.ln
        s = "10" * (self.ln // 2)
        return Number("".join(self.stream[a] if i == "1" else other.stream[a]
                              for a, i in enumerate(s)))

    def __mul__(self, other):
        other = Number(other)
        assert self.ln == other.ln
        return Number("".join("1" if "1" == i == other.stream[a] else "0"
                              for a, i in enumerate(self.stream)))

Number.precision = 1 << 15
p = Number(0.4)
q = Number(0.1)
print(p)
print(q)
print(p + q)
print(p * q)
print(p * q + ~(p * q))
