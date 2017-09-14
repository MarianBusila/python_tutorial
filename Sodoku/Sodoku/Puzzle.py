class Puzzle:
    def __init__(self, grid, rules, **args):
        self.grid = grid
        self._cells = self.grid._cells
        self._regions = self.grid._compute_regions(**args);
        self._cell_regions = self.grid._compute_cell_regions(self._regions, **args)
        self._hidden_cells = []
        self._rules = [rule(self) for rule in rules]

    def compute(self, trace_steps = False, **_):
        if not self._rules: return
        step = 0
        while True:
            rules = self._rules.copy()
            while True:
                rule = random.choice(rules)
                cell2hide = rule.choose_cell()
                if cell2hide: break
                rules.remove(rule)
                if not rules: return
            step += 1
            self._hidden_cells.append(cell2hide)
            for rule in self._rules:
                rule.hide_cell(cell2hide)
            if trace_steps: 
                print('step: {0}, cell2hide: {1}, rule: {2}'.format(step, cell2hide, rule))
                print(self)

    def __repr__(self):
        result = ''
        horizontal_separator =  ('+' + '-' * 3 * 3) * 3 + '+' + os.linesep + '|'
        fmt = ' {0} '

        result += horizontal_separator
        for index, cell in enumerate(self._cells):
            if cell not in self._hidden_cells:
                result += fmt.format(cell.value)
            else:
                result += '   '
            if index % 27 == 26: 
                result += '|' + os.linesep + horizontal_separator
            elif index % 9 == 8:
                result += '|' + os.linesep + '|'
            elif index % 3 == 2:
                result += '|'
        return result[:-1]