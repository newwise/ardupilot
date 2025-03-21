#!/usr/bin/env python
"""
 The standard interface emitters must implement
"""

import re


class Emit:
    def __init__(self, *args, **kwargs):
        pass

    prog_values_field = re.compile(r"\s*(-?\w+:\w+)+,*")

    def close(self):
        pass

    def start_libraries(self):
        pass

    def emit(self, g):
        pass
