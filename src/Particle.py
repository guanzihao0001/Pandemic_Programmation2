import random

import Field
from Position import Direction, Position


class Particle:
    """Represents a particle in movement with a position
    and a direction.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, position: Position, direction: Direction,
                 colour: str, field: Field):
        """Initialize a particle.

        :colour: Particle colour.
        :field: Field containing the particle.
        """
        self.position = position
        self.direction = direction
        self.colour = colour
        self.field = field
        self.cure_sign = 0

    def move(self) -> None:
        """Particle moves to a new position.

        Random move depending on the particle's current position.
        """
        nextPosition = self.field.freeAdjacentPosition(self, 2)
        self.setPosition(nextPosition)

    def setPosition(self, nextPosition: Position) -> None:
        """Place the particle at the given position.
        """
        self.field.clear(self.position)
        self.position = nextPosition
        self.field.place(self)

    def __str__(self):
        return f'Paricle({self.position})'

    def cure(self):
        if self.colour == 'red':
            self.cure_sign += 1
        if self.cure_sign == 21:
            k = random.random()
            if k >= 0.5:
                self.colour = 'black'
                self.cure_sign = 100
            else:
                self.colour = 'spring green'
                self.cure_sign = 100
