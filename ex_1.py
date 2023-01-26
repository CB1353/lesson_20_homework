class Shape:

    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, color):
        self._inner_color = color

    def get_border_color(self):
        return self._border_color

    def set_border_color(self, color):
        self._border_color = color

class Circle(Shape):

    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

class Rectangle(Shape):

    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

class Square(Rectangle):

    def __init__(self, inner_color, border_color, side):
        super().__init__(inner_color, border_color, side, side)

    def set_side(self, side):
        self._width = side
        self._length = side