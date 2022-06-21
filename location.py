MEDIUM_COMMON = {
    "1a": {  # 第一页第一张图
        "hero": (),
        "monkey_ace": (12, 31),
        "sniper_monkey": ()
    },
    "2d": {  # 第一页第一张图
        "hero": (829, 355),
        "monkey_ace": (647, 243),
        "sniper_monkey": (939, 283)
    }
}


class Location:

    def __init__(self, difficulty: str, detail: str):
        self.difficulty = difficulty
        self.detail = detail

    def get_monkeys_location(self, map_id: str):
        if self.difficulty.lower() == "medium":
            if self.detail.lower() in ["standard", "reverse", "military_monkeys_only"]:
                return MEDIUM_COMMON[map_id.lower()]
