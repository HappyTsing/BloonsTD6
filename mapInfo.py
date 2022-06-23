def get_all_map_ids():
    return ['1a', '1b', '1c', '1d', '1e', '1f',
            '2a', '2b', '2c', '2d', '2e', '2f',
            '3a', '3b', '3c', '3d', '3e','3f',
            '4a', "4b",
            '5a', '5b', '5c', '5d', '5e', '5f',
            '6a', '6b', '6c', '6d', '6e', '6f',
            '7a', '7b', '7c', '7d', '7e',
            '8a', '8b', '8c', '8d', '8e', '8f',
            '9a', '9b', '9c', '9d', '9e', '9f',
            '10a',
            '11a', '11b', '11c', '11d', '11e', '11f',
            '12a', '12b', '12c', '12d']


def get_unable_map_ids():
    UNABLE = ['11a', '9c', "8d", "9f"]
    return UNABLE


def get_chimps_map_ids():
    return ['1a', '1b', '1c', '1f']


def get_easy_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b']
    return FINISHED


def get_easy_unfinished_map_ids():
    all_map_ids = get_all_map_ids()
    easy_finished_map_ids = get_easy_finished_map_ids()
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - set(easy_finished_map_ids) - set(unable_map_ids))
    return UNFINISHED


def get_medium_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1d', '1e', '1f',
                '2a', '2b', '2c', '2d', '2e', '2f',
                '3a', '3b', '3c', '3d', '3e','3f',
                '4a', "4b",
                '5a', '5b', '5c', '5d', '5e', '5f',
                '6a', '6b', '6c', '6d', '6e', '6f',
                '7a', '7b', '7c', '7d', '7e',
                '8a', '8b', '8c', '8d', '8e', '8f',
                '9a', '9b', '9c', '9d', '9e', '9f',
                '10a',
                '11a', '11b', '11c', '11d', '11e', '11f',
                '12a', '12b', '12c', '12d']
    return FINISHED


def get_medium_unfinished_map_ids():
    all_map_ids = get_all_map_ids()
    medium_finished_map_ids = get_medium_finished_map_ids()
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - set(medium_finished_map_ids) - set(unable_map_ids))
    return UNFINISHED


def get_hard_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b']
    return FINISHED


def get_hard_unfinished_map_ids():
    all_map_ids = get_all_map_ids()
    hard_finished_map_ids = get_hard_finished_map_ids()
    unable_map_ids = get_unable_map_ids()
    UNFINISHED = list(set(all_map_ids) - set(hard_finished_map_ids) - set(unable_map_ids))
    return UNFINISHED
