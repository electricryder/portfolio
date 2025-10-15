class Jar:
    def __init__(self, capacity=12):
            self.capacity = capacity
            self.size = 0


    def __str__(self):
        from emoji import emojize
        cookie_emoji = emojize(":cookie:", language = "alias")
        return f"{cookie_emoji}" * self.size


    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("The jar is full")
        return self.size


    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("The jar is empty")
        return self.size


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or type(capacity) != int:
            raise ValueError("Invalid capacity")
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar_1 = Jar(100)
    jar_1.deposit(100)
    jar_1.withdraw(30)
    print(jar_1)


if __name__ == "__main__":
    main()
