class NumbersList(list):
    def __init__(self, *args):
        for arg in args:
            if type(arg) not in (int, float):
                raise TypeError('Only numeric values allowed!')
        super().__init__(*args)

    def append(self, item):
        if type(item) not in (int, float):
            raise TypeError('Only numeric values allowed!')
        else:
            super().append(item)

    def extend(self, iterable):
        for item in iterable:
            if type(item) not in (int, float):
                raise TypeError('Only numeric values allowed!')
            else:
                super().extend(iterable)


    def get_sum(self):
        return sum(self)

    def get_average(self):
        return sum(self) / len(self)