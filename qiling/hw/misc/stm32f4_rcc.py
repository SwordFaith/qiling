#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from qiling.hw.peripheral import QlPeripheral


class STM32F4RCC(QlPeripheral):
    def __init__(self, ql, base_addr):
        super().__init__(ql, base_addr)
        self.mem = {}

    def read(self, offset, size):
        ## TODO: Temporary plan, wait for me to implement uart and then change it.
        if offset == 0:
            return b'\xff\xff\x00\x00'
        return b'\x00\x00\x00\x00'
