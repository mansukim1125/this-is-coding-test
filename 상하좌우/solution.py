from typing import List

Direction = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}


class OutOfRangeError(Exception):
    pass


class Map:
    def __init__(self, size: int, move_directions: List[str]):
        self.size = size
        self.move_directions = move_directions
        self.current_coordinate = (1, 1)

    def check_if_out_of_range(self, coordinate: tuple[int]):
        if not (1 <= coordinate[0] <= self.size and 1 <= coordinate[1] <= self.size):
            raise OutOfRangeError

    def move_to(self, direction: str):
        d = Direction[direction]
        next_coordinate = (
            self.current_coordinate[0] + d[0],
            self.current_coordinate[1] + d[1]
        )
        self.check_if_out_of_range(next_coordinate)
        self.current_coordinate = next_coordinate

    def get_destination(self) -> tuple[int]:
        for direction in self.move_directions:
            try:
                self.move_to(direction)
            except OutOfRangeError:
                pass
        return self.current_coordinate


def solution():
    size = int(input())
    move_directions = input().split()
    
    coordinate = Map(size, move_directions).get_destination()
    print(coordinate[0], coordinate[1])


if __name__ == '__main__':
    solution()
    pass
