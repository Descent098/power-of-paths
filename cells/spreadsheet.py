# This file has 2 classes that help represent a Spreadsheet, and the Cells inside them
from typing import Dict, Any, Union
from string import ascii_lowercase
from dataclasses import dataclass, field

@dataclass
class Cell:
    column: str # Start with "a" and go to "z", then add digit i.e. "z" then next column is "aa" then "ab" etc.
    row: int
    content: Any
    
    def __post_init__(self):
        # Validate the column provided is valid
        self.column = self.column.lower()
        for letter in self.column:
            if letter not in ascii_lowercase:
                raise ValueError(f"{letter} is not a valid character for a column")
    
    def convert_column_to_integer(self) -> int:
        """Takes in a column string represenataion, and converts to an integer


        Notes
        -----
        - Essentially the column is base 26, 'a' is 1, 'z' is 26 and then you add\
        a digit for every set of 27 (i.e. 'z' is 26 so 27 is 'aa', then 28 is 'ab' etc.)
        
        Returns
        -------
        int
            The integer representation of the column indicator
        """
        result = 0

        # Start from end of the list since the digits are multiplied by 26 for each digit after the first
        for index, letter in enumerate(self.column[::-1]):
            letter_value = ord(letter) - 96 # Ord starts at 97 for a, so need to subtract 96

            if index > 0: # If not first digit take the letter value and multiply by 26
                multiplier = index*26
                result += multiplier*letter_value
            else:
                result += letter_value
        return result
        

@dataclass
class Spreadsheet:
    cells: Dict[str, Cell] = field(default_factory = lambda: dict())
    rightmost_column: Cell = None # The largest column (farthest right)
    lowest_row: Cell = None # The largest row (lowest down)
    
    def __post_init__(self):
        # Postprocess cells if they were provided so rightmost_column and lowest_row are set
        if self.cells:
            cells_to_add = list(self.cells.values())
            self.cells = dict()
            for cell in cells_to_add:
                self.add_cell(cell)
    
    def add_cell(self, cell:Cell):
        """Allows you to add a cell to the spreadsheet

        Parameters
        ----------
        cell : Cell
            The cell to add to the spreadsheet
        """
        self.cells[f"{cell.column}{cell.row}"] = cell

        if self.rightmost_column:
            if self.rightmost_column.convert_column_to_integer() < cell.convert_column_to_integer():
                self.rightmost_column = cell
        else:
            self.rightmost_column = cell

        if self.lowest_row:
            if self.lowest_row.row < cell.row:
                self.lowest_row = cell
        else:
            self.lowest_row = cell
    
    def find_cell(self, indicator: str) -> Union[Cell, False]:
        """Finds cell based on indicator

        Parameters
        ----------
        indicator : str
            The indicator for the column and row (i.e. 'a4' is column a row 4)

        Returns
        -------
        Union[Cell, False]
            Returns Cell if one exists, else False
        """
        return self.cells.get(indicator, False)
    
if __name__ == "__main__":
    s = Spreadsheet(cells ={"a11": Cell("a",11,"Q"),"aa13": Cell("aa",13,"Z"),"az11": Cell("az",11,"B")})
    print(s)