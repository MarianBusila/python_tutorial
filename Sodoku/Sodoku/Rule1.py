import random

class Rule1:
    'If a region has no hidden cell, we can hide one cell of this region'

    def __init__(self, puzzle):
        self._full_regions = puzzle._regions[:]
        self._cell_regions = puzzle._cell_regions

    def choose_cell(self):
        if not self._full_regions: return None
        full_region = random.choice(self._full_regions)
        return random.choice(full_region._cells)

    def hide_cell(self, cell):
        if not self._full_regions: return
        for cell_region in self._cell_regions[cell]:
            if cell_region in self._full_regions:
                self._full_regions.remove(cell_region)