class Book:
    def __init__(self, title, page_count):
        # The setter is called implicitly here when you assign the value.
        self.title = title
        self.page_count = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        


    @property
    def page_count(self):
        """Getter for page_count."""
        return self._page_count

   
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            # This 'print' statement matches the test's expectation
            print("page_count must be an integer")
        elif value <= 0:
            print("page_count must be a positive number")
        else:
            self._page_count = value
    

   