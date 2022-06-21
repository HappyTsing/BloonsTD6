Python模拟鼠标和键盘可以使用下述方法:

- pyinput
- autopy
- win32api
- vb类似于按键精灵的模式，使用大漠综合插件。

前面三种已经证明不可行，因为都是api层面的操作，一定都会被游戏系统屏蔽。因此使用dm.dll，这也是按键精灵底层使用的方法。

文件位于：`dm/dm.dll`

最后的免费版本dm 3.1233[下载](https://pan.baidu.com/s/1fzUPggaqONCspKzhmV6KLw?pwd=zuc1)

```python
# pywin32版本需要是225（高了可能不行）
pip install pywin32==225 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 管理员模式打开终端
cd /dm
regsvr32 dm.dll
```
此外，需要32位版本的[python](https://www.python.org/ftp/python/3.7.6/python-3.7.6.exe)。

python使用dm代码[参见](https://juejin.cn/post/7065952110625423368)

也可以参考官方文档：`dm/大漠接口说明.CHM`