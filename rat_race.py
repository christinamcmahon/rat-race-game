# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        ''' (Rat, str, int, int) -> NoneType
        A Rat, represented with a 1-character symbol, at a location
        represented by row and col. 
        '''

        self.symbol = symbol
        self.row = row
        self.col = col
        num_sprouts_eaten = 0

    def set_location(self, row, col):
        ''' (Rat, int, int) -> NoneType
        A Rat at a location represented by row and col. 
        '''

        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> NoneType
        Adds one to the rat's num_sprouts_eaten.
        '''

        num_sprouts_eaten = num_sprouts_eaten + 1

    def __str__(self):
        '''(Rat) -> str
        Return a string representation of the rat's symbol, location,
        and number of sprouts eaten. 

        >>> __str__(Rat)
        'J at (4,3) ate 2 sprouts.'
        '''

        Return symbol + ' at (' + row + ',' + col + ') ate ' + num_sprouts_eaten + ' sprout(s).'

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.