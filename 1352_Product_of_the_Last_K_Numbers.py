class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.zero_i = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_i = len(self.products)
            self.products.append(1)
        elif not self.products:
            self.products.append(num)
        else:
            self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if len(self.products) - k <= self.zero_i:
            return 0
        if len(self.products) == k:
            return self.products[-1]
        return self.products[-1] // self.products[-k - 1]


if __name__ == '__main__':
    input1 = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    input2 = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    output = []

    for i, command in enumerate(input1):
        if command == "ProductOfNumbers":
            obj = ProductOfNumbers()
            output.append(None)
        elif command == "add":
            output.append(obj.add(input2[i][0]))
        elif command == "getProduct":
            output.append(obj.getProduct(input2[i][0]))
    print(output)