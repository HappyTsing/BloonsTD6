from time import sleep
from utils import Utils
from location import Location
from dm.dm import DM
from monkey import Monkey
from mapInfo import get_single_map_ids

dm = DM()


def standard(map_id):
    utils = Utils("hard", "standard")
    location = Location("hard", "standard")
    utils.start()
    utils.select(map_id)
    monkey_location = location.get_monkeys_location(map_id)
    hero = Monkey(monkey_location["hero"], "u")
    monkey_ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_monkey = Monkey(monkey_location["sniper_monkey"], "z")
    hero.put()
    dm.keyPress("Space", 2)
    monkey_ace.put()

    sleep(6)
    sniper_monkey.put()
    sniper_monkey.target("strong")
    utils.skill(1)
    sleep(12)

    monkey_ace.update_to("001")
    sleep(9)
    monkey_ace.update_to("002")
    sleep(10)
    for i in range(2):
        sleep(26)
        utils.skill(1)
    sleep(8)
    monkey_ace.update_to("003")
    for i in range(3):
        sleep(2)
        monkey_ace.update_force(path=3)

    sleep(9)
    monkey_ace.update_to("103")
    for i in range(3):
        sleep(2)
        monkey_ace.update_force(path=1)
    sleep(9)
    monkey_ace.update_to("203")
    sleep(9)
    sniper_monkey.update_to("100")
    sleep(4)
    sniper_monkey.update_to("110")
    sleep(5)
    sniper_monkey.update_to("120")
    sleep(18)
    sniper_monkey.update_to("220")
    sleep(28)
    sniper_monkey.update_to("320")
    sleep(36)
    sniper_monkey.update_to("420")
    for i in range(3):
        sleep(10)
        sniper_monkey.update_force(path=1)
    for i in range(4):
        utils.skill(1)
        utils.skill(2)
        sleep(26)
    monkey_ace.update_to("204")
    for i in range(3):
        sleep(10)
        monkey_ace.update_force(path=3)
    sleep(235)
    monkey_ace.update_to("205")
    for i in range(3):
        sleep(10)
        monkey_ace.update_force(path=3)
    sleep(98)
    sniper_monkey.update_to("520")
    sleep(90)  # 85

    if map_id in get_single_map_ids():
        utils.go_on()
        sleep(250)
        dm.click(1500, 500)  # insta 猴子
        sleep(1)
        # 手动激活设置 重新开始 然后在回到主页
        utils.finish(type="esc")
    else:
        utils.finish()


def magic_monkeys_only():
    # todo 魔法猴子
    return False


def double_hp_moabs():
    # todo
    return False


def half_cash():
    # todo
    return False


def alternate_bloons_rounds(map_id):
    utils = Utils("hard", "alternate_bloons_rounds")
    location = Location("hard", "alternate_bloons_rounds")
    utils.start()
    utils.select(map_id)
    monkey_location = location.get_monkeys_location(map_id)
    ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_520 = Monkey(monkey_location["sniper_monkey"], "z")
    sniper_205 = Monkey(monkey_location["hero"], "z")
    ace.put()
    dm.keyPress("Space", 2)
    sniper_205.put()
    sniper_520.put()
    sniper_520.target("strong")
    sniper_205.update_to("001")
    sleep(9)
    sniper_520.update_to("010")
    print("pagedown")
    sniper_520.target("stealth")
    sleep(8)
    ace.update_to("010")
    sleep(5)
    ace.update_to("020")

    sleep(7)
    sniper_205.update_to("002")
    sleep(9)
    sniper_205.update_to("102")

    sleep(12)
    sniper_520.update_to("020")
    sleep(9)
    sniper_520.update_to("120")

    sleep(8)
    ace.update_to("021")
    sleep(5)
    ace.update_to("022")
    sleep(45)
    ace.update_to("023")
    for i in range(3):
        sleep(4)
        ace.update_force(path=3)
    sleep(30)
    sniper_205.update_to("103")
    for i in range(2):
        sleep(3)
        sniper_205.update_force(path=3)
    sleep(12)
    sniper_205.update_to("203")
    for i in range(2):
        sleep(3)
        sniper_205.update_force(path=1)
    sleep(17)
    sniper_205.update_to("204")
    for i in range(2):
        sleep(3)
        sniper_205.update_force(path=3)

    sleep(11)
    sniper_520.update_to("220")
    sleep(25)
    sniper_520.update_to("320")
    sleep(25)
    sniper_520.update_to("420")

    sleep(60)
    ace.update_to("024")
    for i in range(4):
        sleep(8)
        ace.update_force(path=3)

    sleep(60)
    sniper_205.update_to("205")
    for i in range(3):
        sleep(5)
        sniper_205.update_force(path=3)

    sleep(118)
    sniper_520.sale()
    sniper_205.sale()
    ace.update_to("205")
    for i in range(3):
        sleep(5)
        ace.update_force(path=3)
    sleep(35)
    sniper_502 = Monkey(monkey_location["sniper_monkey"], "z")
    sniper_502.put()
    sniper_502.update_to("402")
    sniper_502.target("strong")
    sleep(90)
    sniper_502.update_to("502")
    sleep(80)
    utils.finish()


def impoppable():
    # todo 极难模式
    return False


def chimps():
    # todo 点击模式 感觉没有通用脚本
    return False
