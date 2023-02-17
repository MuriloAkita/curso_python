from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


print(move(Directions.right))
print(move(Directions.left))
print(move(Directions.up))
print(move(Directions.down))
print()

for direction in Directions:
    print(direction, direction.name, direction.value)
