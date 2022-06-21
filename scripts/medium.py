from pymouse import PyMouse
from time import sleep
from utils import Utils
from location import Location
from dm.dm import DM

m = PyMouse()
dm = DM()


def standard(map_id):
    utils = Utils("medium", "standard")
    location = Location("medium", "standard")
    utils.start()
    utils.select(map_id)

    monkey_location = location.get_monkeys_location(map_id)
    print(monkey_location)
    hero = monkey_location["hero"]
    monkey_ace = monkey_location["monkey_ace"]
    sniper_monkey = monkey_location["sniper_monkey"]

    sleep(3)
    dm.KeyPress("u")
    sleep(2)
    m.click(*hero)

    # utils.finish()


standard("2d")


def reverse():
    standard()


def military_monkeys_only():
    standard()


# 天启模式
def apopalypse():
    # todo 天启模式的脚本代码
    return False
