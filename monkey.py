from dm.dm import DM
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


class Monkey:

    # type即猴子的快捷键
    def __init__(self, location: set, monkey: str):
        self.location = location
        self.monkey = monkey
        self.dm = DM()
        # 该参数用于定位target。target_nums % 4 = 0，则说明当前为FIRST，若为1，则当前为LAST
        self.target_nums = 0

    def put(self):
        self.dm.keyPress(self.monkey)
        self.dm.click(*self.location)

    def update(self, path, n=1):
        PATH = {
            1: ",",
            2: ".",
            3: "/",
        }
        self.dm.click(*self.location)

        self.dm.keyPress(PATH[path], n)

        self.dm.keyPress("Esc", 1)

    def update_to(self, final: str):
        PATH = {
            1: ",",
            2: ".",
            3: "/"
        }
        self.dm.click(*self.location)
        path1 = int(final[0])
        path2 = int(final[1])
        path3 = int(final[2])
        self.dm.keyPress(PATH[1], path1, interva=0.05)
        self.dm.keyPress(PATH[2], path2, interva=0.05)
        self.dm.keyPress(PATH[3], path3, interva=0.05)
        self.dm.keyPress("Esc", 1)

    def target(self, target: str):
        TARGET = {
            "first": 0,
            "last": 1,
            "close": 2,
            "strong": 3
        }
        origin_nums = self.target_nums % 4

        # first -> strong   3 - 0 = 3      因此需要按3下tab
        # strong -> last    1 - 3 + 4 = 2  因此需要按2下tab
        n = TARGET[target.lower()] - origin_nums
        if n < 0:
            n = n + 4
        # logging.info("n: " + str(n) + " origin_nums: " + str(origin_nums))
        self.target_nums += n

        self.dm.click(*self.location)
        self.dm.keyPress("Tab", n)
        self.dm.keyPress("Esc", 1)