# Description: Program contains Jar class -> Represents a cookie jar
# > Initializes with a default capacity of 12 and 0 cookies
# > User can deposit or withdraw cookies from the jar -> Capacity cannot be exceeded and jar must contain a positive number of cookies or 0
# > Jar only accepts integer values
# Note: It seems like size was meant to be included in __init__ as the getter was given, otherwise it would be useless. This might be seen as changing the given parameters.

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies to deposit.")
        self.size += n


    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self.size - n < 0:
            raise ValueError("Too many cookies to withdraw.")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Jar must hold 1 or more cookies.")
        if capacity % 1 != 0:
            raise ValueError("Number of cookies must be an integer.")
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size cannot exceed capacity.")
        if size < 0:
            raise ValueError("Jar cannot hold a negative number of cookies.")
        if size % 1 != 0:
            raise ValueError("Number of cookies must be an integer.")
        self._size = size
