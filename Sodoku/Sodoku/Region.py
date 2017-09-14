class Region:
    def __init__(self, cells):
        self._cells = cells

    def __repr__(self):
        return repr(self._cells)

    def remove(self, cell):
        self._cells.remove(cell)
        for c in self._cells:
            if cell.value in c._possible_values:
                c._possible_values.remove(cell.value)