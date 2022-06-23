# 简述

本项目是为了减少bloons td 6的人工成本，在`双金`的前提下，实现如下功能：
- 专家图 炼狱 100 关，刷 insta 猴

- 自动完成：
  - 简单难度
  - 中级难度
  - 困难难度中的 【标准、替代气球回合、双倍生命值MOAB、极难】

理论上来说，无双金也可以使用，不过需要自己修改代码。

本项目将地图定义为`页数+编号`的形式，例如`1a`表示第一页第一张图，而`2f`则代表第二页第六张图。

# 环境

- 1920*1080
- 设置关闭游戏提示

# 安装
```shell
# 32位 python 3.7
pip install -r requirements.txt

# 管理员模式打开终端
cd /dm
regsvr32 dm.dll
```

# 原理

Python模拟鼠标和键盘可以使用下述方法:

- pyinput、autopy、win32api
- vb类似于按键精灵的模式，使用大漠综合插件。

前面三种已经证明不可行，因为都是api层面的操作，一定都会被游戏系统屏蔽。因此选择使用dm.dll，这也是按键精灵底层使用的方法。

> 笔者尝试了 `pyinput`，其有关鼠标的操作可以正常运行，而键盘的操作无法运行。
> 
> 因此本项目采用 `pyinput + dm.dll`结合的方式编写。




# 其他依赖

- 大漠免费版本 [dm 3.1233](https://pan.baidu.com/s/1fzUPggaqONCspKzhmV6KLw?pwd=zuc1)，文件内置于：`dm/dm.dll`

- 32位版本 [python 3.7.6](https://www.python.org/ftp/python/3.7.6/python-3.7.6.exe)。

- python调用dm代码 [教程](https://juejin.cn/post/7065952110625423368)

- 官方文档：`dm/大漠接口说明.CHM`

# 后续工作

- 可适配不同的分辨率