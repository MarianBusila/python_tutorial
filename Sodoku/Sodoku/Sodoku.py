import os
import random

from Grid import Grid
from Puzzle import Puzzle
from Rule1 import Rule1

full_puzzle = '+---------+---------+---------+'\
            '|    9    |       5 | 3     8 |'\
            '|    2    |         |    9    |'\
            '| 8     5 |       9 |         |'\
            '+---------+---------+---------+'\
            '|         |    9    |    3    |'\
            '| 1     9 |         | 4     6 |'\
            '|    8    |    7    |         |'\
            '+---------+---------+---------+'\
            '|         | 7       | 8     1 |'\
            '|    5    |         |    7    |'\
            '| 7     8 | 1       |    6    |'\
            '+---------+---------+---------+'\

simple_puzzle = ' 9   53 8 2     9 8 5  9       9  3 1 9   4 6 8  7       7  8 1 5     7 7 81   6 '
grid = Grid(puzzle = full_puzzle, trace_retry = True)
print (grid)


        