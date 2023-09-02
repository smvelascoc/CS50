class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self._size = 0
        self.deposit(size)

    def __str__(self):
        j = ""
        for _ in range(self.size):
            j = j + "🍪"
        return j

    def deposit(self, n):
        if (self.size + n) <= self.capacity:
            self._size = self.size + n
        else:
            raise ValueError("Capacity overload")

    def withdraw(self, n):
        if (self.size - n) >= 0:
            self._size = self.size - n
        else:
            raise ValueError("Negative capacity")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    #Setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative capacity")
        self._capacity = capacity

    #@size.setter
    #def size(self, size):
        #if (self.capacity() >= size >= 0):
         #   self._size = size
        #else:
          #  raise ValueError("Size overload")

def main():
    print("Test 1")
    jar = Jar()
    print_prop(jar)

    print("Test 2")
    jar.deposit(1)
    print_prop(jar)

    print("Test 3")
    jar.deposit(11)
    print_prop(jar)

    print("Test 4")
    jar.withdraw(10)
    print_prop(jar)

    print("Test5")
    jar2 = Jar(12,6)
    print_prop(jar2)

    print("Test6")
    jar3 = Jar(size=4)
    print_prop(jar3)

    print("Test7")
    try:
        jar4 = Jar(-1)
    except ValueError:
        print("Test 7 passed")

    print("Test8")
    try:
        jar5 = Jar(size=13)
        print_prop(jar5)
    except ValueError:
        print("Test 8 passed")

        print("Test9")
    try:
        jar6 = Jar()
        jar6.withdraw(1)
        print_prop(jar5)
    except ValueError:
        print("Test 9 passed")

def print_prop(jar):
    print(jar)
    print(f"Capacity = {jar.capacity}")
    print(f"Size = {jar.size}")

if __name__ == "__main__":
    main()