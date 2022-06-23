import logging
from scripts.medium import standard as standard_medium, reverse, military_monkeys_only
from scripts.easy import standard as standard_easy, primary_monkeys_only, deflation
from mapInfo import get_easy_unfinished_map_ids, get_medium_unfinished_map_ids, get_hard_unfinished_map_ids
from time import sleep

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def easy_run():
    map_ids_to_finish = get_easy_unfinished_map_ids()
    finished = []
    n = 0
    map_ids_to_finish.sort()
    sleep(2)
    for map_id in map_ids_to_finish:
        if map_id in ['4a', '5e', ]:
            standard_easy(map_id)
        # primary_monkeys_only(map_id)
        # deflation(map_id)
        finished.append(map_id)
        n += 1
        logging.info("【easy】 当前进度: {}/{}  FINISHED: {}".format(n, len(map_ids_to_finish), finished))

def medium_run():
    map_ids_to_finish = get_medium_unfinished_map_ids()
    finished = []
    n = 0
    map_ids_to_finish.sort()
    sleep(2)
    for map_id in map_ids_to_finish:
        print("jjjj")
        standard_medium(map_id)
        military_monkeys_only(map_id)
        reverse(map_id)

        finished.append(map_id)
        n += 1
        logging.info("【medium】当前进度: {}/{}  FINISHED: {}".format(n, len(map_ids_to_finish), finished))
easy_run()