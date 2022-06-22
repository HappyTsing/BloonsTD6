import win32com.client
from time import sleep
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


class DM:
    def __init__(self):
        try:
            self.dm = win32com.client.Dispatch('dm.dmsoft')
            # 3.1233是最后的免费版本
            # print('本机系统中已经安装大漠综合插件，版本为:', self.dm.ver())
        except:
            logging.error('本机并未安装大漠综合插件，需要注册调用')
            raise

    def keyPress(self, key, n=1, interva=0.2):
        for i in range(n):
            self.dm.KeyPressChar(key)
            sleep(interva)

    # pymouse的点击会失效，因此摆放猴子使用dm提供的方式，先移动，再点击。
    def click(self, x: int, y: int, n=1, interva=0.2):
        for i in range(n):
            self.dm.moveto(x, y)
            sleep(interva)
            self.dm.leftclick()
            sleep(interva)
