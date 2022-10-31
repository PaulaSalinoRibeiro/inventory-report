from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            current_value = self.data[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return current_value
