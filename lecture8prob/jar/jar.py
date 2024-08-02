class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Cannot be negative")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n >= 0:
            if n > self.capacity:
                raise ValueError("Jar couldn't fit")
            else:
                self.size += n
                return self.__size
        else:
            raise ValueError("Cannot have negative 🍪")

    def withdraw(self, n):
        if n >= 0:
            if n > self.size:
                raise ValueError("Not enough 🍪 to withdraw")
            else:
                self.size -= n
                return self.__size
        else:
            raise ValueError("Cannot have negative 🍪")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Cannot have negative 🍪")
        self.__capacity = capacity

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Jar couldn't fit")
        self.__size = size


def main():
    jar = Jar()
    print(jar.capacity)  # default 12
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)  # 3

    """
    jar.capacity = -1 --> triggers capacity.setter
    jar.size = 100 --> triggers size.setter if size > capacity
    jar1 = Jar(5)
    print(jar1.capacity) # 5
    """


if __name__ == "__main__":
    main()
