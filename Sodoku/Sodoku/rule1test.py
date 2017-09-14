import unittest

import ruletest
import Sodoku


class Rule1Test(ruletest.RuleTest):
    'If a region has no hidden cell, we can hide one cell of this region'

    def setUp(self):
        super().setUp()
        self._rule_type = Sodoku.Rule1


    def test_column0(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '| 1       |         |         |'\
            '| 2       |         |         |'\
            '| 3       |         |         |'\
            '+---------+---------+---------+'\
            '| 4       |         |         |'\
            '| 5       |         |         |'\
            '| 6       |         |         |'\
            '+---------+---------+---------+'\
            '| 7       |         |         |'\
            '| 8       |         |         |'\
            '| 9       |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 0)


    def test_column1(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|    1    |         |         |'\
            '|    2    |         |         |'\
            '|    3    |         |         |'\
            '+---------+---------+---------+'\
            '|    4    |         |         |'\
            '|    5    |         |         |'\
            '|    6    |         |         |'\
            '+---------+---------+---------+'\
            '|    7    |         |         |'\
            '|    8    |         |         |'\
            '|    9    |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 1)


    def test_column2(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|       1 |         |         |'\
            '|       2 |         |         |'\
            '|       3 |         |         |'\
            '+---------+---------+---------+'\
            '|       4 |         |         |'\
            '|       5 |         |         |'\
            '|       6 |         |         |'\
            '+---------+---------+---------+'\
            '|       7 |         |         |'\
            '|       8 |         |         |'\
            '|       9 |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 2)


    def test_column3(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         | 1       |         |'\
            '|         | 2       |         |'\
            '|         | 3       |         |'\
            '+---------+---------+---------+'\
            '|         | 4       |         |'\
            '|         | 5       |         |'\
            '|         | 6       |         |'\
            '+---------+---------+---------+'\
            '|         | 7       |         |'\
            '|         | 8       |         |'\
            '|         | 9       |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 3)


    def test_column4(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |    1    |         |'\
            '|         |    2    |         |'\
            '|         |    3    |         |'\
            '+---------+---------+---------+'\
            '|         |    4    |         |'\
            '|         |    5    |         |'\
            '|         |    6    |         |'\
            '+---------+---------+---------+'\
            '|         |    7    |         |'\
            '|         |    8    |         |'\
            '|         |    9    |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 4)


    def test_column5(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |       1 |         |'\
            '|         |       2 |         |'\
            '|         |       3 |         |'\
            '+---------+---------+---------+'\
            '|         |       4 |         |'\
            '|         |       5 |         |'\
            '|         |       6 |         |'\
            '+---------+---------+---------+'\
            '|         |       7 |         |'\
            '|         |       8 |         |'\
            '|         |       9 |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 5)


    def test_column6(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         | 1       |'\
            '|         |         | 2       |'\
            '|         |         | 3       |'\
            '+---------+---------+---------+'\
            '|         |         | 4       |'\
            '|         |         | 5       |'\
            '|         |         | 6       |'\
            '+---------+---------+---------+'\
            '|         |         | 7       |'\
            '|         |         | 8       |'\
            '|         |         | 9       |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 6)


    def test_column7(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |    1    |'\
            '|         |         |    2    |'\
            '|         |         |    3    |'\
            '+---------+---------+---------+'\
            '|         |         |    4    |'\
            '|         |         |    5    |'\
            '|         |         |    6    |'\
            '+---------+---------+---------+'\
            '|         |         |    7    |'\
            '|         |         |    8    |'\
            '|         |         |    9    |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 7)


    def test_column8(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |       1 |'\
            '|         |         |       2 |'\
            '|         |         |       3 |'\
            '+---------+---------+---------+'\
            '|         |         |       4 |'\
            '|         |         |       5 |'\
            '|         |         |       6 |'\
            '+---------+---------+---------+'\
            '|         |         |       7 |'\
            '|         |         |       8 |'\
            '|         |         |       9 |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_column(self.cell2hide, 8)


    def test_row0(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 0)


    def test_row1(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 1)


    def test_row2(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 2)


    def test_row3(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 3)


    def test_row4(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 4)


    def test_row5(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 5)


    def test_row6(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 6)


    def test_row7(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 7)


    def test_row8(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '| 1  2  3 | 4  5  6 | 7  8  9 |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_row(self.cell2hide, 8)


    def test_square0(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '| 1  2  3 |         |         |'\
            '| 4  5  6 |         |         |'\
            '| 7  8  9 |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 0)


    def test_square1(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         | 1  2  3 |         |'\
            '|         | 4  5  6 |         |'\
            '|         | 7  8  9 |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 1)


    def test_square2(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         | 1  2  3 |'\
            '|         |         | 4  5  6 |'\
            '|         |         | 7  8  9 |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 2)


    def test_square3(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '| 1  2  3 |         |         |'\
            '| 4  5  6 |         |         |'\
            '| 7  8  9 |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 3)


    def test_square4(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         | 1  2  3 |         |'\
            '|         | 4  5  6 |         |'\
            '|         | 7  8  9 |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 4)


    def test_square5(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         | 1  2  3 |'\
            '|         |         | 4  5  6 |'\
            '|         |         | 7  8  9 |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 5)


    def test_square6(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '| 1  2  3 |         |         |'\
            '| 4  5  6 |         |         |'\
            '| 7  8  9 |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 6)


    def test_square7(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         | 1  2  3 |         |'\
            '|         | 4  5  6 |         |'\
            '|         | 7  8  9 |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 7)


    def test_square8(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         | 1  2  3 |'\
            '|         |         | 4  5  6 |'\
            '|         |         | 7  8  9 |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assert_square(self.cell2hide, 8)


    def test_nomorerowcell(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|    2  3 | 4  5  6 | 7  8  9 |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assertIsNone(self.cell2hide)


    def test_nomorecolumncell(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '| 2       |         |         |'\
            '| 3       |         |         |'\
            '+---------+---------+---------+'\
            '| 4       |         |         |'\
            '| 5       |         |         |'\
            '| 6       |         |         |'\
            '+---------+---------+---------+'\
            '| 7       |         |         |'\
            '| 8       |         |         |'\
            '| 9       |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assertIsNone(self.cell2hide)


    def test_nomoresquarecell(self):
        #Arrange
        self.set_puzzle(\
            '+---------+---------+---------+'\
            '|    2  3 |         |         |'\
            '| 4  5  6 |         |         |'\
            '| 7  8  9 |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            '|         |         |         |'\
            '|         |         |         |'\
            '|         |         |         |'\
            '+---------+---------+---------+'\
            )

        #Act
        self.cell2hide = self.rule.choose_cell()

        #Assert
        self.assertIsNone(self.cell2hide)



if __name__ == '__main__':
    unittest.main()