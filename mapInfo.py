def get_all_map_ids():
    all_map_ids = []
    for i in range(12):
        n = i + 1
        if n == 4:
            js = ['a', 'b']
        elif n == 7:
            js = ['a', 'b', 'c', 'd', 'e']
        elif n == 10:
            js = ['a']
        else:
            js = ['a', 'b', 'c', 'd', 'e', 'f']
        for j in js:
            map_id = str(n) + j
            all_map_ids.append(map_id)
    return all_map_ids


def get_chimps_map_ids():
    return ['1a', '1b', '1c', '1f']


def get_easy_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b']
    return  FINISHED


def get_medium_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b']
    return  FINISHED


def get_hard_finished_map_ids():
    FINISHED = ['1a', '1b', '1c', '1c', '1e', '1f', '2a', '2b', '2c', '2d', '2e', '2f', '3c', '5c', '11d', '11e', '12b']
    return  FINISHED