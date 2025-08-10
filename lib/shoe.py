class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    def cobble(self):
        self.condition="New"
        print("Your shoe is as good as new!")
        
    @property
    def size(self):
        # The getter must return the private attribute, self._size
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value