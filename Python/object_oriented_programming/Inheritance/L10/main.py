class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def get_area(self) -> int:
        return self.length * self.width

    def get_perimeter(self) -> int:
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)

    
