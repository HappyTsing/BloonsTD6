import win32com.client
class DM:
    def __init__(self):
        try:
            self.dm = win32com.client.Dispatch('dm.dmsoft')
            # 3.1233是最后的免费版本
            print('本机系统中已经安装大漠插件，版本为:', self.dm.ver())
        except:
            print('本机并未安装大漠，需要注册调用')

    def KeyPress(self, key):
        self.dm.KeyPressChar(key)
