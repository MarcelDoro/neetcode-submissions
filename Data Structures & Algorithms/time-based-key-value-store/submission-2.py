class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        full_key = (key, timestamp)
        self.TimeMap[full_key] = value

    def get(self, key: str, timestamp: int) -> str:
        full_key = (key, timestamp)
        exist = self.TimeMap.get(full_key, False)
        if exist != False:
            return self.TimeMap[full_key]
        else:
            i = timestamp - 1
            while i >= 0:
                full_key = (key, i)
                exist = self.TimeMap.get(full_key, False)
                if exist != False:
                    return self.TimeMap[full_key]
                i -= 1

            return ""
