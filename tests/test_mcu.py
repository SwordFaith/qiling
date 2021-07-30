#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#


import sys, unittest
sys.path.append("..")

from qiling.core import Qiling
from qiling.const import QL_VERBOSE

class MCUTest(unittest.TestCase):
    def test_mcu_led_stm32f411(self):
        ql = Qiling(["../examples/rootfs/stm32f411/hex/rand_blink.hex"],                    
                    archtype="cortex_m", profile="stm32f411", verbose=QL_VERBOSE.DISASM)

        # Set verbose=QL_VERBOSE.DEFAULT to find warning
        ql.run(count=1000)

        del ql

    def test_mcu_usart_output_stm32f411(self):
        ql = Qiling(["../examples/rootfs/stm32f411/hex/hello_usart.hex"],                    
                    archtype="cortex_m", profile="stm32f411", verbose=QL_VERBOSE.DEFAULT)
        
        # create/remove
        ql.hw.create('USART', 'usart2', 0x40023800)
        ql.hw.create('STM32F4RCC', 'rcc', 0x40023800)
        ql.run(count=2000)

        del ql

if __name__ == "__main__":
    unittest.main()

