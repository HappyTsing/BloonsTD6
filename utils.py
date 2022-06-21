from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep

m = PyMouse()
k = PyKeyboard()


class Utils:

    def __init__(self, difficulty, detail):
        self.difficulty = difficulty
        self.detail = detail

    def start(self):
        sleep(3)
        m.click(827, 931, 1)
        sleep(2)

    def next_pages(self, num: int):
        # 重置为第一页，首先点击中级，再点击新手即可
        m.click(850, 1000, 1)
        sleep(1)
        m.click(550, 1000, 1)
        sleep(1)

        for i in range(num):
            m.click(1650, 430, 1)
            sleep(1)

    def choose_map(self, position: str):
        MAP_POSITION = {
            "a": (500, 250),
            "b": (1000, 250),
            "c": (1500, 250),
            "d": (500, 500),
            "e": (1000, 500),
            "f": (1500, 500)
        }
        position = MAP_POSITION[position.lower()]
        m.click(position[0], position[1], 1)
        sleep(1)

    def choose_difficulty(self):
        DIFFICULTY_POSITION = {
            "easy": (650, 400),
            "medium": (1000, 400),
            "hard": (1300, 400)
        }
        EASY_POSITION = {
            "standard": (650, 550),
            "primary_monkeys_only": (950, 450),
            "deflation": (1250, 450)
        }
        MEDIUM_POSITION = {
            "standard": (650, 550),
            "military_monkeys_only": (950, 450),
            "apopalypse": (1250, 450),
            "reverse": (950, 750),

        }

        HARD_POSITION = {
            "standard": (650, 600),
            "magic_monkeys_only": (950, 450),
            "double_hp_moabs": (1250, 450),
            "half_cash": (1600, 450),
            "alternate_bloons_rounds": (950, 750),
            "impoppable": (1250, 750),
            "chimps": (1600, 750),
        }

        difficulty_position = DIFFICULTY_POSITION[self.difficulty.lower()]
        m.click(difficulty_position[0], difficulty_position[1], 1)
        sleep(1)

        if self.difficulty.lower() == "easy":
            m.click(EASY_POSITION[self.detail.lower()][0], EASY_POSITION[self.detail.lower()][1], 1)
        elif self.difficulty.lower() == "medium":
            m.click(MEDIUM_POSITION[self.detail.lower()][0], MEDIUM_POSITION[self.detail.lower()][1], 1)
        elif self.difficulty.lower() == "hard":
            m.click(HARD_POSITION[self.detail.lower()][0], HARD_POSITION[self.detail.lower()][1], 1)
        else:
            raise
        sleep(5)

    def select(self, map_id: str):
        # 1. 翻页
        page_num = int(map_id[0:len(map_id) - 1])
        self.next_pages(page_num - 1)

        # 2. 选择地图
        map_position = map_id[len(map_id) - 1]
        self.choose_map(map_position.lower())

        # 3. 选择难度
        self.choose_difficulty()

    def finish(self):
        # 下一页
        m.click(970, 904, 1)
        sleep(1)

        # 主页
        m.click(688, 838,1)
        sleep(4)
