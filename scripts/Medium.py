from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep


def standard():
    m = PyMouse()
    k = PyKeyboard()

    # # 按住alt键
    # k.press_key(k.alt_key)
    # # tab键
    # k.tap_key(k.tab_key)
    # # 释放alt键
    # k.release_key(k.alt_key)

    # 第几页
    PAGES = [1, 3]
    # 开始
    sleep(3)
    m.click(827, 931, 1)
    sleep(2)

    # 下一页
    for i in range(1):
        m.click(1649, 432, 1)
        sleep(1)

    m.click(500, 250, 1)


def reverse():
    standard()


def military_monkeys_only():
    standard()


# 天启模式
def apopalypse():
    # todo 天启模式的脚本代码
    return False
