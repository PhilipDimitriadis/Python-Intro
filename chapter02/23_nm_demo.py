class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self.__y = y
    
    def __str__(self):
        return f"({self._x}, {self.__y})"


def main():
    p1 = Point(11, 20)
    print(p1)

    print(p1._x)
    p1.__y = 100
    print(p1.__y)
    # print(p1._Point__y)
    print(p1)

    p1.thanasis = 1000

    print(p1.thanasis)

if __name__ == "__main__":
    main()