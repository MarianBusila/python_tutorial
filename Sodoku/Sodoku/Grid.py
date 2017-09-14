import os
import random

from Cell import Cell
from Region import Region
from Puzzle import Puzzle

class Grid:
    def __init__(self, puzzle=None, trace_retry = False):
        done = False
        while not done:
            try:
                if puzzle is not None:
                    puzzle = Grid.trim_puzzle(puzzle)
                    assert(len(puzzle) == 81)
                    self._cells = [ Cell(row, column, Grid._get_value(puzzle[row * 9 + column])) for row in range(9) for column in range(9)]
                else:
                    self._cells = [ Cell(row, column, None) for row in range(9) for column in range(9)]

                self._compute(trace_compute = False, trace_regions = False)
                done = True
            except IndexError as error:
                if trace_retry:
                    print ("Exception: " + str(error.args) + ". Retrying")

    def _get_value(value):
        if value == '\xa0' or value == ' ': # is space
            return None;
        else:
            return int(value)

    def trim_puzzle(puzzle):
        if not puzzle: return 81 * ' '
        if puzzle[0] != '+': return puzzle
        result = ''
        for square_row in range(3):
            for row in range(4 * square_row + 1, 4 * square_row + 4):
                for col in range(2, 31, 10):
                    result += puzzle[31 * row + col:31 * row + col + 9:3]
        return result

    def create_puzzle(self, *rules, **args):
        return Puzzle(self, list(rules), **args)

    def compute_puzzle(self, *rules, **args):
        result = self.create_puzzle(*rules, **args)
        result.compute(**args)
        return result

    def _dump(self, show_possibilities = True):
        result = ""
        intersection_sep = "+"
        vertical_sep = "|"
        horizontal_sep = "-"
        
        if show_possibilities:
            cell_width = 33
            cell_format = " {0:^9} "
        else:
            cell_width = 9
            cell_format = " {0} "
        
        horizontal_separator = (intersection_sep + horizontal_sep * cell_width) * 3 + intersection_sep + os.linesep
        result +=  horizontal_separator
        result += vertical_sep
        for index, cell in enumerate(self._cells):
            if cell.value:
                result +=  cell_format.format(str(cell.value))
            else:
                result +=  cell_format.format(str(cell._possible_values)[1:-1:3])

            if index % 3 == 2:
                result += vertical_sep

            if index % 27 == 26:
                result += os.linesep + horizontal_separator

            if index % 9  == 8:
                result += os.linesep + vertical_sep
        
        return result[:-1]

    def __repr__(self):
        return self._dump(show_possibilities = False)

    def _compute_regions(self, trace_regions = False, **_):    
        rows = [Region(self._cells[row:row+9]) for row in range(0,81,9)]
        if trace_regions:
            print ("Rows regions:")
            print (rows)


        columns = [Region(self._cells[column::9]) for column in range(9)]
        if trace_regions:
            print ("Columns regions:")
            print (columns)
        

        boxes = [Region([cell for cell in self._cells if cell._id[0] // 3 == row and cell._id[1] // 3 == col]) 
                for row in range(3) 
                for col in range(3)]

        if trace_regions:
            print ("Boxes regions:")
            print (boxes)

        return rows + columns + boxes

    def _compute_cell_regions (self, regions = None, **args):        
        if not regions: regions = self._compute_regions(**args)
        cell_regions = {cell:[] for cell in self._cells}
        
        for region in regions:
            for cell in region._cells:
                cell_regions[cell].append(region);

        return cell_regions

    def _fix_one_cell(self, cell_regions):
        random_cell = self. _select_most_contrained_cell()
        random_cell.choose_value()
        for region in cell_regions[random_cell]:
            region.remove(random_cell)

    def _compute(self, trace_compute = False, **args):                
        cell_regions = self._compute_cell_regions(**args)
        for i in range(81):
            self._fix_one_cell(cell_regions)
        
        if trace_compute:
            print (self)
        
    def _select_most_contrained_cell(self):
        most_contrained_cells = []
        min_possibilities = 9
        for cell in self._cells:
            if cell.value == None:
                if len(cell._possible_values) < min_possibilities:
                    most_contrained_cells = [cell]
                    min_possibilities = len(cell._possible_values)
                elif len(cell._possible_values) == min_possibilities:
                    most_contrained_cells.append(cell)
        
        return random.choice(most_contrained_cells)