def get_all_map_ids():
    return ['1a', '1b', '1c', '1d', '1e', '1f',
            '2a', '2b', '2c', '2d', '2e', '2f',
            '3a', '3b', '3c', '3d', '3e', '3f',
            '4a', "4b",
            '5a', '5b', '5c', '5d', '5e', '5f',
            '6a', '6b', '6c', '6d', '6e', '6f',
            '7a', '7b', '7c', '7d', '7e',
            '8a', '8b', '8c', '8d', '8e', '8f',
            '9a', '9b', '9c', '9d', '9e', '9f',
            '10a',
            '11a', '11b', '11c', '11d', '11e', '11f',
            '12a', '12b', '12c', '12d']


def get_single_map_ids():
    return ['1a', '1b', '1c', '1d', '1e', '1f',
            '2a', '2b', '2c', '2d', '2e', '2f',
            '3a', '3b', '3c', '3d', '3e', '3f',
            '4a', "4b",
            '5b',
            '6b', '6c', '6e',
            '7a', '7b', '7e',
            '8a', '8b', '8c', '8d', '8e', '8f']


def get_unable_map_ids():
    # 8d:齿轮转动 9c:高级金融 9f：玉米地 11a：避难所
    UNABLE = ["8d", '9c', "9f", '11a']
    return UNABLE


def get_chimps_map_ids():
    return ['1a', '1b', '1c', '1f']


def get_easy_unfinished_map_ids():
    all_map_ids = get_all_map_ids()
    FINISHED = {'1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b'}
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - FINISHED - set(unable_map_ids))
    return UNFINISHED


def get_medium_unfinished_map_ids():
    all_map_ids = get_all_map_ids()
    FINISHED = {'1a', '1b', '1c', '1d', '1e', '1f',
                '2a', '2b', '2c', '2d', '2e', '2f',
                '3a', '3b', '3c', '3d', '3e', '3f',
                '4a', "4b",
                '5a', '5b', '5c', '5d', '5e', '5f',
                '6a', '6b', '6c', '6d', '6e', '6f',
                '7a', '7b', '7c', '7d', '7e',
                '8a', '8b', '8c', '8d', '8e', '8f',
                '9a', '9b', '9c', '9d', '9e', '9f',
                '10a',
                '11a', '11b', '11c', '11d', '11e', '11f',
                '12a', '12b', '12c', '12d'}
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - FINISHED - set(unable_map_ids))
    return UNFINISHED


def get_hard_unfinished_map_ids(difficulty: str):
    # HARD_UNABLE中是当前脚本无法通关，（主要原因是路太短，铅气球只有狙击猴打，来不及。解决办法是 可以在空档期添加一个103的狙击猴，不过特地写脚本太麻烦了，就手动打吧。
    HARD_UNABLE = ['5d', '6c', '10a', '11b', '11c', '11f']

    FINISHED = {
        "standard": {'1a', '1b', '1c', '1d', '1e', '1f',
                     '2a', '2b', '2c', '2d', '2e', '2f',
                     '3a', '3b', '3c', '3d', '3e', '3f',
                     '4a', "4b",
                     '5a', '5b', '5c', '5d', '5e', '5f',
                     '6a', '6b', '6c', '6d', '6e', '6f',
                     '7a', '7b', '7c', '7d', '7e',
                     '8a', '8b', '8c', '8d', '8e', '8f',
                     '9a', '9b', '9c', '9d', '9e', '9f',
                     '10a',
                     '11a', '11b', '11c', '11d', '11e', '11f',
                     '12a', '12b', '12c', '12d'},
        "magic_monkeys_only": {},
        "double_hp_moabs": {},
        "half_cash": {},
        "alternate_bloons_rounds": {'1a', '1b', '1c', '1d', '1e', '1f',
                                    '2a', '2b', '2c', '2d', '2e', '2f',
                                    '3a', '3b', '3c', '3d', '3e', '3f',
                                    '4a', "4b",
                                    '5a', '5b', '5c', '5e', '5f',
                                    '6a', '6b', '6d', '6e', '6f',
                                    '7a', '7b', '7c', '7d', '7e',
                                    '8a', '8b', "8c", '8e', '8f',
                                    '11c', '11d', '11e',
                                    '9a', '9b', '9d', '9e',
                                    '12a', '12b', '12c', '12d'},
        "impoppable": {},
        "chimps": {}
    }
    all_map_ids = get_all_map_ids()
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - set(FINISHED[difficulty]) - set(unable_map_ids) - set(HARD_UNABLE))
    return UNFINISHED
