from heapq import heappop, heappush

class StockPrice:
    def __init__(self):
        self.latest_time = 0
        # Store price of each stock at each timestamp.
        self.timestamp_price_map = {}
        
        # Store stock prices in sorted order to get min and max price.
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update latestTime to latest timestamp.
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        # Add latest price for timestamp.
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Return latest price of the stock.
        return self.timestamp_price_map[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while -price != self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
            
        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]

        # Pop pairs from heap with the price doesn't match with hashmap.
        while price != self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
            
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


if __name__ == '__main__':
    input1 = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
    input2 = [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
    output = []

    for i, command in enumerate(input1):
        if command == "StockPrice":
            obj = StockPrice()
            output.append(None)
        elif command == "update":
            output.append(obj.update(input2[i][0], input2[i][1]))

        elif command == "current":
            output.append(obj.current())
        elif command == "maximum":
            output.append(obj.maximum())
        elif command == "minimum":
            output.append(obj.minimum())

    print(output)