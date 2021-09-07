import sys
sys.path.append("../..")

from qiling.core import Qiling
from qiling.const import QL_VERBOSE


def h_addr(ql, addr, data):
    print('---------------------')
    for i in range(0, 8):
        r = ql.reg.read('r'+str(i))
        print(f'r{str(i)} = {hex(r)}')
    print('---------------------')

def test_mcu_gpio_stm32f411():
    ql = Qiling(["../../examples/rootfs/mcu/stm32f411/hello_gpioA.hex"],                    
                archtype="cortex_m", profile="stm32f411", verbose=QL_VERBOSE.DEBUG)

    ql.hw.create('usart2')
    ql.hw.create('rcc')
    ql.hw.create('gpioa')

    ql.hw.gpioa.hook_set(5, lambda: print('LED light up'))
    ql.hw.gpioa.hook_reset(5, lambda: print('LED light off'))

    ql.run(count=10000)

if __name__ == "__main__":
    test_mcu_gpio_stm32f411()