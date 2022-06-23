from time import sleep
from utils import Utils
from location import Location
from dm.dm import DM
from monkey import Monkey

dm = DM()


def common_run(map_id, location):
    monkey_location = location.get_monkeys_location(map_id)
    hero = Monkey(monkey_location["hero"], "u")
    monkey_ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_monkey = Monkey(monkey_location["sniper_monkey"], "z")
    hero.put()
    dm.keyPress("Space", 2)
    sniper_monkey.put()
    sniper_monkey.update_to("001")
    sniper_monkey.target("strong")
    sleep(25)
    monkey_ace.put()
    sleep(13)
    monkey_ace.update_to("001")
    sleep(8)
    monkey_ace.update_to("002")
    sleep(70)
    monkey_ace.update_to("003")
    sleep(30)
    monkey_ace.update_to("203")
    sleep(40)
    sniper_monkey.update_to("202")
    sleep(30)
    sniper_monkey.update_to("203")
    sleep(30)
    sniper_monkey.update_to("204")
    sleep(140)
    monkey_ace.update_to("204")
    sleep(90)
    sniper_monkey.update_to("205")
    sleep(110)


def standard(map_id):
    utils = Utils("medium", "standard")
    location = Location("medium", "standard")
    utils.start()
    utils.select(map_id)
    common_run(map_id, location)
    utils.finish()


def reverse(map_id):
    utils = Utils("medium", "reverse")
    location = Location("medium", "reverse")
    utils.start()
    utils.select(map_id)
    common_run(map_id, location)
    utils.finish()


def military_monkeys_only(map_id):
    utils = Utils("medium", "military_monkeys_only")
    location = Location("medium", "military_monkeys_only")
    utils.start()
    utils.select(map_id)
    common_run(map_id, location)
    utils.finish()


# 天启模式
def apopalypse(map_id):
    utils = Utils("medium", "apopalypse")
    location = Location("medium", "apopalypse")
    utils.start()
    utils.select(map_id)
    monkey_location = location.get_monkeys_location(map_id)

    hero = Monkey(monkey_location["hero"], "u")
    monkey_ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_monkey = Monkey(monkey_location["sniper_monkey"], "z")

    hero.put()
    dm.keyPress("Space", 1)
    monkey_ace.put()

    sniper_monkey.put()
    sniper_monkey.target("strong")
    sleep(33)
    monkey_ace.update_to("001")
    sleep(22)
    monkey_ace.update_to("002")
    sleep(36)
    sniper_monkey.update_to("001")
    sleep(15)
    sniper_monkey.update_to("002")
    sleep(65)
    monkey_ace.update_to("003")
    sleep(5)
    sniper_monkey.update_to("102")
    sleep(20)
    monkey_ace.update_to("023")
    sleep(45)
    sniper_monkey.update_to("103")
    sleep(75)
    sniper_monkey.update_to("104")
    sleep(25)
    sniper_monkey.update_to("204")
    utils.finish()

