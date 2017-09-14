import random

class Cell:    
    def __init__(self, row, column, value):
        self._id = (row, column)
        if value is None:
            self._possible_values = list(range(1, 10))
        else:
            self._possible_values = [value]
        self.value = None
    
    def __repr__(self):
        return repr(self._id)

    def choose_value(self, trace_choose_value  = False, **_):
        self.value = random.choice(self._possible_values)
        if trace_choose_value:
            print ("Choose value:" + self._id + " ->" + self.value)
