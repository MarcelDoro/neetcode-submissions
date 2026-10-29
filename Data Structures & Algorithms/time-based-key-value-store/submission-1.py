class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        full_key = (key, timestamp)
        self.TimeMap[full_key] = value

    def get(self, key: str, timestamp: int) -> str:
        full_key = (key, timestamp)
        if full_key in self.TimeMap:
            return self.TimeMap[full_key]
        else:
            i = timestamp - 1
            while i >= 0:
                full_key = (key, i)
                if full_key in self.TimeMap:
                    return self.TimeMap[full_key]
                i -= 1

            return ""
