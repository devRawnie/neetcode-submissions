class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # print(key, timestamp, self.d)
        if key not in self.d:
            return ""

        values = self.d[key]
        l = 0
        r = len(values)-1

        while r - l > 1:
            m = l + (r-l)//2
            if values[m][1] == timestamp:
                return values[m][0]

            if timestamp < values[m][1]:
                r = m - 1
            else:
                l = m

        if values[r][1] <= timestamp:
            return values[r][0]
        if values[l][1] <= timestamp:
            return values[l][0]

        return ""
