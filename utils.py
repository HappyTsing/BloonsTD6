from pymouse import PyMouse
from time import sleep
from dm.dm import DM

m = PyMouse()
dm = DM()


class Utils:

    def __init__(self, difficulty: str, detail: str):
        self.difficulty = difficulty
        self.detail = detail

    def start(self):
        sleep(3)
        m.click(827, 931)
        sleep(2)

    def choose_page(self, page_number: int):
        # 重置为第一页，首先点击中级，再点击新手即可
        m.click(850, 1000)
        sleep(1)
        m.click(550, 1000)
        sleep(1)

        if page_number in [1, 2, 3, 4]:
            for i in range(page_number - 1):
                m.click(550, 1000)
                sleep(1)
        elif page_number in [5, 6, 7]:
            for i in range(page_number - 4):
                m.click(850, 1000)
                sleep(1)
        elif page_number in [8, 9, 10]:
            for i in range(page_number - 7):
                m.click(1100, 1000)
                sleep(1)
        elif page_number in [11, 12]:
            for i in range(page_number - 10):
                m.click(1350, 1000)
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
        m.click(*position)
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
        m.click(*difficulty_position)
        sleep(1)

        if self.difficulty.lower() == "easy":
            m.click(*EASY_POSITION[self.detail.lower()])
        elif self.difficulty.lower() == "medium":
            m.click(*MEDIUM_POSITION[self.detail.lower()])
        elif self.difficulty.lower() == "hard":
            m.click(*HARD_POSITION[self.detail.lower()])
        else:
            raise
        sleep(5)
        if self.detail.lower() == "apopalypse":
            m.click(950, 750)
            sleep(1.5)

    def select(self, map_id: str):
        # 1. 翻页
        page_number = int(map_id[0:len(map_id) - 1])
        self.choose_page(page_number)

        # 2. 选择地图
        map_position = map_id[len(map_id) - 1]
        self.choose_map(map_position.lower())

        # 3. 选择难度
        self.choose_difficulty()

    def finish(self, type="common"):
        if type == "common":
            # 下一页
            m.click(970, 904, 1)
            sleep(1)

            # 主页
            m.click(688, 838, 1)
            sleep(4)
        elif type == "esc":
            dm.keyPress("Esc")
            sleep(1)
            # 重新开始
            m.click(1050, 850, 1)
            # 确定重新开始
            m.click(1100, 710, 1)
            dm.keyPress("Esc")
            # 主页
            m.click(850, 850, 1)
            sleep(4)

    def go_on(self):
        m.click(950, 900, 1)
        sleep(1)
        m.click(1200, 850, 1)
        sleep(1)
        m.click(1200, 850, 1)
        sleep(1)
        dm.keyPress("Space")
        sleep(1)

    def skill(self, n: int):
        dm.keyPress(str(n), n=1, interva=0)
