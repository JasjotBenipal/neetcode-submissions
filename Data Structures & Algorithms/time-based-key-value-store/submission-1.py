class TimeMap:

    def __init__(self):
        self.values = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key][timestamp] = value
        if "Listing" in self.values[key]:
            self.values[key]["Listing"].append(timestamp)
        else:
            self.values[key]["Listing"] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.values[key]:
            return self.values[key][timestamp]

        res = ""
        left = 0
        listing = self.values[key].get("Listing", [])
        right = len(listing) - 1
        print(right)
        while left <= right:
            mid = (left + right) // 2

            if listing[mid] < timestamp:
                res = self.values[key][listing[mid]]
                left = mid + 1
            else:
                right = mid - 1
        return res

