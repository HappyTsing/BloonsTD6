import logging
from scripts.medium import standard, reverse, military_monkeys_only
from mapInfo import get_all_map_ids, get_medium_finished_map_ids
from time import sleep

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

all_map_ids = get_all_map_ids()
medium_finished_map_ids = get_medium_finished_map_ids()
map_ids_to_finish = list(set(all_map_ids) - set(medium_finished_map_ids))
finished = []
n = 0
map_ids_to_finish.sort()
sleep(2)
for map_id in map_ids_to_finish:
    standard(map_id)
    military_monkeys_only(map_id)
    reverse(map_id)
    finished.append(map_id)
    n += 1
    logging.info("当前进度: {}/{}  FINISHED: {}".format(n, len(map_ids_to_finish), finished))
