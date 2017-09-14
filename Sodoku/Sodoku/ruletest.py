import unittest

from Sodoku import *


class RuleTest(unittest.TestCase):


    def setUp(self):
        self.cell2hide = None


    def tearDown(self):
        if self.cell2hide:
            self.assertIn(self.cell2hide, self._grid._cells)


    def get_cell(self, row, column):
        return self._grid._cells[row * 9 + column]


    def hide_cell(self, cell):
        self.rule.hide_cell(cell)
        self.puzzle._hidden_cells.append(cell)


    def hide_cell_at(self, row, column):
        self.hide_cell(self.get_cell(row, column))


    def set_puzzle(self, puzzle):
        puzzle = Grid.trim_puzzle(puzzle)
        self._grid = Grid(puzzle)
        self.puzzle = self._grid.create_puzzle(self._rule_type)
        self.rule = self.puzzle._rules[0]
        for index, c in enumerate(puzzle):
            if c == ' ':
                self.hide_cell(self.puzzle._cells[ index ])


    def assert_column(self, cell, column):
        self.assertEqual(cell._id[1], column, 'Cell is ' + str(cell._id));


    def assert_row(self, cell, row):
        self.assertEqual(cell._id[0], row, 'Cell is ' + str(cell._id));


    def assert_square(self, cell, square):
        self.assertEqual(cell._id[0] // 3, square // 3, 'Cell is ' + str(cell._id))
        self.assertEqual(cell._id[1] // 3, square % 3, 'Cell is ' + str(cell._id))


    def assert_value(self, cell, value):
        self.assertEqual(cell.value, value, 'Cell is ' + str(cell._id))
