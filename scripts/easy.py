from time import sleep
from utils import Utils
from location import Location
from dm.dm import DM
from monkey import Monkey
dm = DM()

def standard(map_id):
    utils = Utils("easy", "standard")
    location = Location("easy", "standard")
    utils.start()
    utils.select(map_id)
    monkey_location = location.get_monkeys_location(map_id)
    hero = Monkey(monkey_location["hero"], "u")
    monkey_ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_monkey = Monkey(monkey_location["sniper_monkey"], "z")
    hero.put()
    dm.keyPress("Space", 2)
    monkey_ace.put()
    sniper_monkey.put()
    sniper_monkey.update_to("001")
    sniper_monkey.target("strong")
    sleep(19)
    monkey_ace.update_to("001")
    sleep(10)
    monkey_ace.update_to("002")
    sleep(60)
    monkey_ace.update_to("003")
    sleep(30)
    monkey_ace.update_to("203")
    sleep(40)
    sniper_monkey.update_to("202")
    sleep(30)
    sniper_monkey.update_to("203")
    sleep(30)
    sniper_monkey.update_to("204")
    sleep(85)
    sniper_monkey.update_to("205")
    sleep(35)
    utils.finish()


def primary_monkeys_only(map_id):
    # todo 太麻烦了
    return False


def deflation(map_id):
    utils = Utils("easy", "deflation")
    location = Location("easy", "deflation")
    utils.start()
    utils.select(map_id)
    monkey_location = location.get_monkeys_location(map_id)
    hero = Monkey(monkey_location["hero"], "u")
    monkey_ace = Monkey(monkey_location["monkey_ace"], "v")
    sniper_monkey = Monkey(monkey_location["sniper_monkey"], "z")
    hero.put()
    dm.keyPress("Space", 2)
    hero.update_to("300")
    monkey_ace.put()
    monkey_ace.update_to("024")
    sniper_monkey.put()
    sniper_monkey.update_to("204")
    sniper_monkey.target("strong")
    utils.finish()
