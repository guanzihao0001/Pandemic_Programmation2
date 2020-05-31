import random
import time

from Field import Field
from Particle import Particle
from Position import Direction, Position
from Randomizer import Randomizer
from SimulatorView import SimulatorView
from State import State


class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    :author: ZHENG Yannan
    """

    def __init__(self, root: object, size=50, num_particle=50):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._particles = []  # all particles in the simulation
        self._field = Field(size)
        self.step = 0
        self._view = SimulatorView(root, size)
        self._colours = {State.SUSCEPTIBLE: 'slate blue',
                         State.INFECTED: 'red',
                         State.RECOVERED: 'spring green',
                         State.DEAD: 'black'}
        self.reset(num_particle)

    def Collision(self, num_particle):
        for p in range(num_particle - 1):
            for q in range(p, num_particle):
                if abs(self._particles[p].position.row - self._particles[q].position.row) + abs(
                        self._particles[p].position.col - self._particles[q].position.col) == 2:
                    if self._particles[p].colour == 'red' and self._particles[q].colour == 'slate blue':
                        self._particles[q].colour = 'red'
                    if self._particles[q].colour == 'red' and self._particles[p].colour == 'slate blue':
                        self._particles[p].colour = 'red'

    def runLongSimulation(self) -> None:
        """Run the simulation from its current state for a reasonably
        long period, e.g. 500 steps.
        """
        self.simulate(500)

    def simulate(self, numSteps, delay=1) -> None:
        """Run the simulation from its current state for
        the given number of steps.

        :delay: Time (in secs) between each iteration.
        """

        self.step = 1
        while self.step <= numSteps:
            self.simulateOneStep()
            # self.step += 1
            time.sleep(delay)

    def simulateOneStep(self) -> None:
        """Run the simulation from its current state for a single step.
        """
        self.step += 1
        #  all _particles in motion
        for particle in self._particles:
            if particle.colour != 'black':
                if particle.colour == 'red' or 'slate blue':
                    particle.move()
                    particle.cure()
                if particle.colour == 'spring green':
                    particle.move()
        self._view.showStatus(self.step, self._particles)
        self.Collision(50)

    def reset(self, num_particle):
        """Reset the simulation to a starting position.
        """
        self.step = 0
        self._particles = []
        self.populate(num_particle)
        self._view.showStatus(self.step, self._particles)

    def populate(self, num_particle=50):
        """Populates the _field with randomly-positioned _particles.
        """
        self._field.clear()
        particle_new = Particle(Position(max=self.size), Direction(), self._colours.get(State.INFECTED), self._field)
        self._particles.append(particle_new)
        for p in range(num_particle - 1):
            position = Position(max=self.size)  # generate 0 <= random Position < size
            direction = Direction()
            color = self._colours.get(State.SUSCEPTIBLE)
            particle_new = Particle(position, direction, color, self._field)
            self._particles.append(particle_new)
            # generate random -1 <= random Direction < 1
            # store particle with position and direction
