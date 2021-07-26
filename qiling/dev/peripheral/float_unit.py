#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from .peripheral import Peripheral

class FloatingPointUnit(Peripheral):
    def __init__(self, ql):
        super().__init__(ql)

    ## TODO: Implement specific details

    @property
    def name(self):
        return 'FPU'
